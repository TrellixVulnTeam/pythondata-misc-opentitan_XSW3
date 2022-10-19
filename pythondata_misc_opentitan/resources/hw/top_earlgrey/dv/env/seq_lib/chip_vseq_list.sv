// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

`include "chip_callback_vseq.sv"
`include "chip_base_vseq.sv"
`include "chip_stub_cpu_base_vseq.sv"
`include "chip_common_vseq.sv"
`include "chip_jtag_csr_rw_vseq.sv"
`include "chip_jtag_mem_vseq.sv"
// This needs to be listed prior to all sequences that derive from it.
`include "chip_sw_base_vseq.sv"
`include "chip_sw_uart_smoke_vseq.sv"
`include "chip_jtag_base_vseq.sv"
`include "chip_prim_tl_access_vseq.sv"
`include "chip_sw_all_escalation_resets_vseq.sv"
`include "chip_sw_clkmgr_escalation_reset_vseq.sv"
`include "chip_sw_full_aon_reset_vseq.sv"
`include "chip_sw_deep_power_glitch_vseq.sv"
`include "chip_sw_main_power_glitch_vseq.sv"
`include "chip_sw_sysrst_ctrl_vseq.sv"
`include "chip_sw_random_sleep_all_reset_vseq.sv"
`include "chip_sw_deep_sleep_all_reset_vseq.sv"
`include "chip_sw_uart_tx_rx_vseq.sv"
`include "chip_sw_uart_rand_baudrate_vseq.sv"
`include "chip_sw_sysrst_ctrl_inputs_vseq.sv"
`include "chip_sw_sysrst_ctrl_reset_vseq.sv"
`include "chip_sw_sysrst_ctrl_outputs_vseq.sv"
`include "chip_sw_sysrst_ctrl_ec_rst_l_vseq.sv"
`include "chip_sw_gpio_smoke_vseq.sv"
`include "chip_sw_gpio_vseq.sv"
`include "chip_sw_flash_ctrl_lc_rw_en_vseq.sv"
`include "chip_sw_flash_init_vseq.sv"
`include "chip_sw_flash_rma_unlocked_vseq.sv"
`include "chip_sw_lc_ctrl_kmac_reset_vseq.sv"
`include "chip_sw_lc_ctrl_transition_vseq.sv"
`include "chip_sw_lc_walkthrough_vseq.sv"
`include "chip_sw_lc_walkthrough_testunlocks_vseq.sv"
`include "chip_sw_spi_tx_rx_vseq.sv"
`include "chip_sw_spi_host_tx_rx_vseq.sv"
`include "chip_sw_rom_ctrl_integrity_check_vseq.sv"
`include "chip_sw_sram_ctrl_execution_main_vseq.sv"
`include "chip_sw_sram_ctrl_scrambled_access_vseq.sv"
`include "chip_sw_sleep_pin_mio_dio_val_vseq.sv"
`include "chip_sw_sleep_pin_wake_vseq.sv"
`include "chip_sw_sleep_pin_retention_vseq.sv"
`include "chip_sw_pwm_pulses_vseq.sv"
`include "chip_sw_keymgr_key_derivation_vseq.sv"
`include "chip_sw_ast_clk_outputs_vseq.sv"
`include "chip_sw_sensor_ctrl_status_intr_vseq.sv"
`include "chip_sw_pwrmgr_deep_sleep_all_wake_ups_vseq.sv"
`include "chip_sw_adc_ctrl_sleep_debug_cable_wakeup_vseq.sv"
`include "chip_tap_straps_vseq.sv"
`include "chip_sw_repeat_reset_wkup_vseq.sv"
`include "chip_sw_rstmgr_alert_info_vseq.sv"
`include "chip_rv_dm_ndm_reset_vseq.sv"
`include "chip_sw_alert_handler_escalation_vseq.sv"
`include "chip_sw_alert_handler_entropy_vseq.sv"
`include "chip_sw_alert_handler_lpg_clkoff_vseq.sv"
`include "chip_sw_lc_ctrl_program_error_vseq.sv"
`include "chip_sw_entropy_src_fuse_vseq.sv"
`include "chip_sw_csrng_lc_hw_debug_en_vseq.sv"
`include "chip_sw_usb_ast_clk_calib_vseq.sv"
`include "chip_sw_i2c_host_tx_rx_vseq.sv"
`include "chip_sw_rv_core_ibex_lockstep_glitch.sv"
`include "chip_sw_inject_scramble_seed_vseq.sv"
`include "chip_sw_exit_test_unlocked_bootstrap_vseq.sv"
`include "chip_sw_patt_ios_vseq.sv"
