// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

#include "sw/device/lib/crypto/drivers/aes.h"

#include "sw/device/lib/base/memory.h"
#include "sw/device/lib/runtime/log.h"
#include "sw/device/lib/testing/test_framework/check.h"
#include "sw/device/lib/testing/test_framework/ottf_main.h"

static const char kSecretKey[] = "Secret test key.";

static const char kPlaintext[] =
    "Muchos años después, frente al pelotón de fusilamiento, el coronel "
    "Aureliano Buendía había de recordar aquella tarde remota en que su "
    "padre lo llevó a conocer el hielo.";

// AES-CTR encrypted using all zeroes IV.
static const uint32_t kCiphertext[] = {
    0x141cf4f1, 0xdcbf3c9b, 0x41c1e909, 0x0202d9f7, 0x27000325, 0x882033f3,
    0xd77b0a50, 0x92425836, 0x72733658, 0x3f80eeef, 0x250086fe, 0x1f015d22,
    0x7054e010, 0xaef95ca9, 0xb446fd50, 0x6bef787d, 0x564e1dcc, 0xe3650cc0,
    0xa75a3298, 0xa0e7a3b8, 0x7d91ca73, 0x034ea236, 0x6cc76e1c, 0xb6b333ab,
    0x4989dfa4, 0x41a7e22b, 0x5d41f04f, 0x7b49b3c6, 0x127e7daa, 0x081306e0,
    0x60d9450c, 0xc7e08a02, 0x353f0dc2, 0x59e33d60, 0x35900057, 0xec8901d5,
    0xb28a4979, 0x52340cc1, 0x95ca3392, 0xfc4d8a32, 0x981cd522, 0x7dab4b1e,
    0xc3352eb6, 0x008ee548, 0x00000000, 0x00000000,
};

const test_config_t kTestConfig;
bool test_main(void) {
  // This is a weak share intended to exercise correct configuration of the
  // hardware; in general, the key should be generated by either generating
  // two shares and setting key = a ^ b, or generating a mask and setting
  // a = key ^ mask, b = mask.
  uint32_t share0[4];
  uint32_t share1[4];
  memcpy(share0, kSecretKey, ARRAYSIZE(kSecretKey));
  for (int i = 0; i < ARRAYSIZE(share0); ++i) {
    if (i % 2 == 0) {
      share0[i] = ~share0[i];
      share1[i] = -1;
    } else {
      share1[i] = ~share0[i];
      share0[i] = -1;
    }
  }

  LOG_INFO("Configuring the AES hardware.");
  CHECK(aes_begin((aes_params_t){
            .encrypt = true,
            .mode = kAesCipherModeCtr,
            .key_len = kAesKeyLen128,
            .key = {share0, share1},
            .iv = {0},
        }) == kAesOk);

  // NOTE: ARRAYSIZE(kPlaintext) is not a multiple of the block size!
  uint32_t ciphertext[ARRAYSIZE(kCiphertext)] = {0};
  char *cipherptr = (char *)&ciphertext[0];
  for (size_t i = 0;; i += sizeof(aes_block_t)) {
    LOG_INFO("Processing block %d.", i / sizeof(aes_block_t));
    size_t bytes_left = ARRAYSIZE(kPlaintext) - i;
    size_t len = sizeof(aes_block_t);
    if (len > bytes_left) {
      len = bytes_left;
    }
    size_t bytes_left_prev = ARRAYSIZE(kPlaintext) - i + sizeof(aes_block_t);
    size_t len_prev = sizeof(aes_block_t);
    if (len_prev > bytes_left_prev) {
      len_prev = bytes_left_prev;
    }
    LOG_INFO("Block len: %d/%d.", len, len_prev);

    aes_block_t in = {0};
    aes_block_t out = {0};
    if (i == 0) {
      memcpy(&in, &kPlaintext[i], len);
      CHECK(aes_update(NULL, &in) == kAesOk);
    } else if (i >= ARRAYSIZE(kPlaintext)) {
      CHECK(aes_update(&out, NULL) == kAesOk);
      memcpy(cipherptr + i - sizeof(out), &out, len_prev);
      break;
    } else {
      memcpy(&in, &kPlaintext[i], len);
      CHECK(aes_update(&out, &in) == kAesOk);
      memcpy(cipherptr + i - sizeof(out), &out, len_prev);
    }
  }
  CHECK_ARRAYS_EQ(ciphertext, kCiphertext, ARRAYSIZE(kCiphertext));

  LOG_INFO("Cleaning up.");
  CHECK(aes_end() == kAesOk);

  return true;
}
