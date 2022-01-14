// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

#include "sw/device/lib/runtime/otbn.h"

#include "sw/device/lib/base/mmio.h"
#include "sw/device/lib/dif/dif_base.h"
#include "sw/device/lib/dif/dif_otbn.h"
#include "sw/device/lib/runtime/log.h"

/**
 * Data width of big number subset, in bytes.
 */
const int kOtbnWlenBytes = 256 / 8;

otbn_result_t otbn_data_ptr_to_dmem_addr(const otbn_t *ctx, otbn_ptr_t ptr,
                                         uint32_t *dmem_addr_otbn) {
  uintptr_t ptr_addr = (uintptr_t)ptr;
  uintptr_t app_dmem_data_start_addr = (uintptr_t)ctx->app.dmem_data_start;
  uintptr_t app_dmem_data_end_addr = (uintptr_t)ctx->app.dmem_data_end;
  uintptr_t app_dmem_bss_start_addr = (uintptr_t)ctx->app.dmem_bss_start;
  uintptr_t app_dmem_bss_end_addr = (uintptr_t)ctx->app.dmem_bss_end;
  uintptr_t app_dmem_bss_offset = (uintptr_t)ctx->app.dmem_bss_offset;

  if (dmem_addr_otbn == NULL || ptr == NULL || ctx == NULL) {
    return kOtbnBadArg;
  }

  if (app_dmem_data_start_addr <= ptr_addr &&
      ptr_addr < app_dmem_data_end_addr) {
    // Pointer is in the data section, which is at the start of DMEM
    *dmem_addr_otbn = ptr_addr - app_dmem_data_start_addr;
  } else if (app_dmem_bss_start_addr <= ptr_addr &&
             ptr_addr < app_dmem_bss_end_addr) {
    // Pointer is in the bss section, which is after the data section
    *dmem_addr_otbn = ptr_addr - app_dmem_bss_start_addr + app_dmem_bss_offset;
  } else {
    // Pointer is not in a valid DMEM region
    return kOtbnBadArg;
  }

  return kOtbnOk;
}

otbn_result_t otbn_busy_wait_for_done(otbn_t *ctx) {
  bool busy = true;
  while (busy) {
    dif_otbn_status_t status;
    if (dif_otbn_get_status(&ctx->dif, &status) != kDifOk) {
      return kOtbnError;
    }
    busy = status != kDifOtbnStatusIdle && status != kDifOtbnStatusLocked;
  }

  dif_otbn_err_bits_t err_bits;
  if (dif_otbn_get_err_bits(&ctx->dif, &err_bits) != kDifOk) {
    return kOtbnError;
  }
  if (err_bits != kDifOtbnErrBitsNoError) {
    return kOtbnOperationFailed;
  }
  return kOtbnOk;
}

otbn_result_t otbn_init(otbn_t *ctx, mmio_region_t base_addr) {
  if (ctx == NULL) {
    return kOtbnBadArg;
  }

  ctx->app_is_loaded = false;

  if (dif_otbn_init(base_addr, &ctx->dif) != kDifOk) {
    return kOtbnError;
  }

  return kOtbnOk;
}

/**
 * Checks if the OTBN application's IMEM and DMEM address parameters are valid.
 *
 * IMEM and DMEM ranges must not be "backwards" in memory, with the end address
 * coming before the start address, and the IMEM range must additionally be
 * non-empty. Finally, separate sections in DMEM must not overlap each other
 * when converted to DMEM address space.
 *
 * @param app the OTBN application to check
 * @return true if the addresses are valid, otherwise false.
 */
bool check_app_address_ranges(const otbn_app_t *app) {
  // IMEM must have a strictly positive range (cannot be backwards or empty)
  if (app->imem_end <= app->imem_start) {
    return false;
  }
  // Both DMEM sections must not be backwards
  if (app->dmem_data_end < app->dmem_data_start ||
      app->dmem_bss_end < app->dmem_bss_start) {
    return false;
  }
  // The offset of BSS in DMEM address space must be at least as large as the
  // data section (i.e. the sections do not overlap in DMEM)
  if (app->dmem_bss_offset < app->dmem_data_end - app->dmem_data_start) {
    return false;
  }
  return true;
}

otbn_result_t otbn_load_app(otbn_t *ctx, const otbn_app_t app) {
  if (!check_app_address_ranges(&app)) {
    return kOtbnBadArg;
  }

  const size_t imem_size = app.imem_end - app.imem_start;
  const size_t data_size = app.dmem_data_end - app.dmem_data_start;

  // Memory images and offsets must be multiples of 32b words.
  if (imem_size % sizeof(uint32_t) != 0 || data_size % sizeof(uint32_t) != 0 ||
      (size_t)app.dmem_bss_offset % sizeof(uint32_t) != 0) {
    return kOtbnBadArg;
  }

  ctx->app_is_loaded = false;
  ctx->app = app;

  if (dif_otbn_imem_write(&ctx->dif, 0, ctx->app.imem_start, imem_size) !=
      kDifOk) {
    return kOtbnError;
  }

  // Zero all of DMEM
  otbn_result_t err = otbn_zero_data_memory(ctx);
  if (err != kOtbnOk) {
    return err;
  }

  // Write initialized data
  if (data_size > 0) {
    if (dif_otbn_dmem_write(&ctx->dif, 0, ctx->app.dmem_data_start,
                            data_size) != kDifOk) {
      return kOtbnError;
    }
  }

  ctx->app_is_loaded = true;
  return kOtbnOk;
}

otbn_result_t otbn_execute(otbn_t *ctx) {
  if (ctx == NULL || !ctx->app_is_loaded) {
    return kOtbnBadArg;
  }

  if (dif_otbn_write_cmd(&ctx->dif, kDifOtbnCmdExecute) != kDifOk) {
    return kOtbnError;
  }

  return kOtbnOk;
}

otbn_result_t otbn_copy_data_to_otbn(otbn_t *ctx, size_t len_bytes,
                                     const void *src, otbn_ptr_t dest) {
  if (ctx == NULL || dest == NULL) {
    return kOtbnBadArg;
  }

  uint32_t dest_dmem_addr;
  otbn_result_t result = otbn_data_ptr_to_dmem_addr(ctx, dest, &dest_dmem_addr);
  if (result != kOtbnOk) {
    return result;
  }

  if (dif_otbn_dmem_write(&ctx->dif, dest_dmem_addr, src, len_bytes) !=
      kDifOk) {
    return kOtbnError;
  }
  return kOtbnOk;
}

otbn_result_t otbn_copy_data_from_otbn(otbn_t *ctx, size_t len_bytes,
                                       otbn_ptr_t src, void *dest) {
  if (ctx == NULL || dest == NULL) {
    return kOtbnBadArg;
  }

  uint32_t src_dmem_addr;
  otbn_result_t result = otbn_data_ptr_to_dmem_addr(ctx, src, &src_dmem_addr);
  if (result != kOtbnOk) {
    return result;
  }

  if (dif_otbn_dmem_read(&ctx->dif, src_dmem_addr, dest, len_bytes) != kDifOk) {
    return kOtbnError;
  }
  return kOtbnOk;
}

otbn_result_t otbn_zero_data_memory(otbn_t *ctx) {
  if (ctx == NULL) {
    return kOtbnBadArg;
  }

  size_t dmem_size_words =
      dif_otbn_get_dmem_size_bytes(&ctx->dif) / sizeof(uint32_t);
  bool retval = kOtbnOk;
  for (size_t i = 0; i < dmem_size_words; ++i) {
    const uint32_t zero = 0;

    // Continue the process even if a single write fails to try to clear as much
    // memory as possible.
    if (dif_otbn_dmem_write(&ctx->dif, i * sizeof(uint32_t), &zero,
                            sizeof(zero)) != kDifOk) {
      retval = kOtbnError;
    }
  }
  return retval;
}

otbn_result_t otbn_dump_dmem(const otbn_t *ctx, uint32_t max_addr) {
  if (ctx == NULL || max_addr % kOtbnWlenBytes != 0 ||
      max_addr > dif_otbn_get_dmem_size_bytes(&ctx->dif)) {
    return kOtbnBadArg;
  }

  if (max_addr == 0) {
    max_addr = dif_otbn_get_dmem_size_bytes(&ctx->dif);
  }

  for (int i = 0; i < max_addr; i += kOtbnWlenBytes) {
    uint32_t data[kOtbnWlenBytes / sizeof(uint32_t)];
    dif_otbn_dmem_read(&ctx->dif, i, data, kOtbnWlenBytes);

    LOG_INFO("DMEM @%04d: 0x%08x%08x%08x%08x%08x%08x%08x%08x",
             i / kOtbnWlenBytes, data[7], data[6], data[5], data[4], data[3],
             data[2], data[1], data[0]);
  }

  return kOtbnOk;
}
