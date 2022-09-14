// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

`include "kmac_base_vseq.sv"
`include "kmac_smoke_vseq.sv"
`include "kmac_common_vseq.sv"
`include "kmac_long_msg_and_output_vseq.sv"
`include "kmac_sideload_vseq.sv"
`include "kmac_test_vectors_base_vseq.sv"
`include "kmac_test_vectors_sha3_vseq.sv"
`include "kmac_test_vectors_shake_vseq.sv"
`include "kmac_test_vectors_kmac_vseq.sv"
`include "kmac_test_vectors_kmac_xof_vseq.sv"
`include "kmac_burst_write_vseq.sv"
`include "kmac_app_vseq.sv"
`include "kmac_app_with_partial_data_vseq.sv"
`include "kmac_entropy_refresh_vseq.sv"
`include "kmac_error_vseq.sv"
`include "kmac_key_error_vseq.sv"
`include "kmac_edn_timeout_error_vseq.sv"
`include "kmac_entropy_mode_error_vseq.sv"
`include "kmac_lc_escalation_vseq.sv"
`include "kmac_stress_all_vseq.sv"
