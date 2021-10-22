// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

#ifndef OPENTITAN_SW_DEVICE_LIB_DIF_AUTOGEN_DIF_ADC_CTRL_AUTOGEN_H_
#define OPENTITAN_SW_DEVICE_LIB_DIF_AUTOGEN_DIF_ADC_CTRL_AUTOGEN_H_

// This file is auto-generated.

/**
 * @file
 * @brief <a href="/hw/ip/adc_ctrl/doc/">ADC_CTRL</a> Device Interface Functions
 */

#include <stdbool.h>
#include <stdint.h>

#include "sw/device/lib/base/macros.h"
#include "sw/device/lib/base/mmio.h"
#include "sw/device/lib/dif/dif_base.h"

#ifdef __cplusplus
extern "C" {
#endif  // __cplusplus

/**
 * A handle to adc_ctrl.
 *
 * This type should be treated as opaque by users.
 */
typedef struct dif_adc_ctrl {
  /**
   * The base address for the adc_ctrl hardware registers.
   */
  mmio_region_t base_addr;
} dif_adc_ctrl_t;

/**
 * Creates a new handle for a(n) adc_ctrl peripheral.
 *
 * This function does not actuate the hardware.
 *
 * @param base_addr The MMIO base address of the adc_ctrl peripheral.
 * @param[out] adc_ctrl Out param for the initialized handle.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_init(mmio_region_t base_addr,
                               dif_adc_ctrl_t *adc_ctrl);

/**
 * A adc_ctrl interrupt request type.
 */
typedef enum dif_adc_ctrl_irq {
  /**
   * USB-C debug cable is attached or disconnected
   */
  kDifAdcCtrlIrqDebugCable = 0,
} dif_adc_ctrl_irq_t;

/**
 * A snapshot of the state of the interrupts for this IP.
 *
 * This is an opaque type, to be used with the `dif_adc_ctrl_irq_get_state()`
 * function.
 */
typedef uint32_t dif_adc_ctrl_irq_state_snapshot_t;

/**
 * Returns the state of all interrupts (i.e., pending or not) for this IP.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param[out] snapshot Out-param for interrupt state snapshot.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_get_state(
    const dif_adc_ctrl_t *adc_ctrl,
    dif_adc_ctrl_irq_state_snapshot_t *snapshot);

/**
 * Returns whether a particular interrupt is currently pending.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param irq An interrupt request.
 * @param[out] is_pending Out-param for whether the interrupt is pending.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_is_pending(const dif_adc_ctrl_t *adc_ctrl,
                                         dif_adc_ctrl_irq_t irq,
                                         bool *is_pending);

/**
 * Acknowledges all interrupts, indicating to the hardware that all
 * interrupts have been successfully serviced.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_acknowledge_all(const dif_adc_ctrl_t *adc_ctrl);

/**
 * Acknowledges a particular interrupt, indicating to the hardware that it has
 * been successfully serviced.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param irq An interrupt request.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_acknowledge(const dif_adc_ctrl_t *adc_ctrl,
                                          dif_adc_ctrl_irq_t irq);

/**
 * Forces a particular interrupt, causing it to be serviced as if hardware had
 * asserted it.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param irq An interrupt request.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_force(const dif_adc_ctrl_t *adc_ctrl,
                                    dif_adc_ctrl_irq_t irq);

/**
 * A snapshot of the enablement state of the interrupts for this IP.
 *
 * This is an opaque type, to be used with the
 * `dif_adc_ctrl_irq_disable_all()` and `dif_adc_ctrl_irq_restore_all()`
 * functions.
 */
typedef uint32_t dif_adc_ctrl_irq_enable_snapshot_t;

/**
 * Checks whether a particular interrupt is currently enabled or disabled.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param irq An interrupt request.
 * @param[out] state Out-param toggle state of the interrupt.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_get_enabled(const dif_adc_ctrl_t *adc_ctrl,
                                          dif_adc_ctrl_irq_t irq,
                                          dif_toggle_t *state);

/**
 * Sets whether a particular interrupt is currently enabled or disabled.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param irq An interrupt request.
 * @param state The new toggle state for the interrupt.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_set_enabled(const dif_adc_ctrl_t *adc_ctrl,
                                          dif_adc_ctrl_irq_t irq,
                                          dif_toggle_t state);

/**
 * Disables all interrupts, optionally snapshotting all enable states for later
 * restoration.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param[out] snapshot Out-param for the snapshot; may be `NULL`.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_disable_all(
    const dif_adc_ctrl_t *adc_ctrl,
    dif_adc_ctrl_irq_enable_snapshot_t *snapshot);

/**
 * Restores interrupts from the given (enable) snapshot.
 *
 * @param adc_ctrl A adc_ctrl handle.
 * @param snapshot A snapshot to restore from.
 * @return The result of the operation.
 */
OT_WARN_UNUSED_RESULT
dif_result_t dif_adc_ctrl_irq_restore_all(
    const dif_adc_ctrl_t *adc_ctrl,
    const dif_adc_ctrl_irq_enable_snapshot_t *snapshot);

#ifdef __cplusplus
}  // extern "C"
#endif  // __cplusplus

#endif  // OPENTITAN_SW_DEVICE_LIB_DIF_AUTOGEN_DIF_ADC_CTRL_AUTOGEN_H_
