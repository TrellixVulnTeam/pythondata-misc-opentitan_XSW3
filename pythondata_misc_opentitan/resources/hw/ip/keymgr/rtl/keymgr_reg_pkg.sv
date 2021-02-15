// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// Register Package auto-generated by `reggen` containing data structure

package keymgr_reg_pkg;

  // Param list
  parameter int NumInReg = 4;
  parameter int NumOutReg = 8;
  parameter int NumKeyVersion = 1;
  parameter int NumAlerts = 2;

  // Address width within the block
  parameter int BlockAw = 8;

  ////////////////////////////
  // Typedefs for registers //
  ////////////////////////////
  typedef struct packed {
    logic        q;
  } keymgr_reg2hw_intr_state_reg_t;

  typedef struct packed {
    logic        q;
  } keymgr_reg2hw_intr_enable_reg_t;

  typedef struct packed {
    logic        q;
    logic        qe;
  } keymgr_reg2hw_intr_test_reg_t;

  typedef struct packed {
    struct packed {
      logic        q;
      logic        qe;
    } fatal_fault_err;
    struct packed {
      logic        q;
      logic        qe;
    } recov_operation_err;
  } keymgr_reg2hw_alert_test_reg_t;

  typedef struct packed {
    struct packed {
      logic        q;
    } start;
    struct packed {
      logic [2:0]  q;
    } operation;
    struct packed {
      logic [1:0]  q;
    } dest_sel;
  } keymgr_reg2hw_control_reg_t;

  typedef struct packed {
    logic        q;
  } keymgr_reg2hw_sideload_clear_reg_t;

  typedef struct packed {
    logic [15:0] q;
  } keymgr_reg2hw_reseed_interval_reg_t;

  typedef struct packed {
    logic        q;
    logic        qe;
  } keymgr_reg2hw_sw_binding_regwen_reg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_sw_binding_mreg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_salt_mreg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_key_version_mreg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_max_creator_key_ver_reg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_max_owner_int_key_ver_reg_t;

  typedef struct packed {
    logic [31:0] q;
  } keymgr_reg2hw_max_owner_key_ver_reg_t;

  typedef struct packed {
    struct packed {
      logic        q;
    } invalid_op;
    struct packed {
      logic        q;
    } invalid_cmd;
    struct packed {
      logic        q;
    } invalid_kmac_input;
    struct packed {
      logic        q;
    } invalid_kmac_data;
  } keymgr_reg2hw_err_code_reg_t;


  typedef struct packed {
    logic        d;
    logic        de;
  } keymgr_hw2reg_intr_state_reg_t;

  typedef struct packed {
    logic        d;
  } keymgr_hw2reg_cfg_regwen_reg_t;

  typedef struct packed {
    struct packed {
      logic        d;
      logic        de;
    } start;
  } keymgr_hw2reg_control_reg_t;

  typedef struct packed {
    logic        d;
  } keymgr_hw2reg_sw_binding_regwen_reg_t;

  typedef struct packed {
    logic [31:0] d;
    logic        de;
  } keymgr_hw2reg_sw_share0_output_mreg_t;

  typedef struct packed {
    logic [31:0] d;
    logic        de;
  } keymgr_hw2reg_sw_share1_output_mreg_t;

  typedef struct packed {
    logic [2:0]  d;
    logic        de;
  } keymgr_hw2reg_working_state_reg_t;

  typedef struct packed {
    logic [1:0]  d;
    logic        de;
  } keymgr_hw2reg_op_status_reg_t;

  typedef struct packed {
    struct packed {
      logic        d;
      logic        de;
    } invalid_op;
    struct packed {
      logic        d;
      logic        de;
    } invalid_cmd;
    struct packed {
      logic        d;
      logic        de;
    } invalid_kmac_input;
    struct packed {
      logic        d;
      logic        de;
    } invalid_kmac_data;
  } keymgr_hw2reg_err_code_reg_t;


  ///////////////////////////////////////
  // Register to internal design logic //
  ///////////////////////////////////////
  typedef struct packed {
    keymgr_reg2hw_intr_state_reg_t intr_state; // [420:420]
    keymgr_reg2hw_intr_enable_reg_t intr_enable; // [419:419]
    keymgr_reg2hw_intr_test_reg_t intr_test; // [418:417]
    keymgr_reg2hw_alert_test_reg_t alert_test; // [416:413]
    keymgr_reg2hw_control_reg_t control; // [412:407]
    keymgr_reg2hw_sideload_clear_reg_t sideload_clear; // [406:406]
    keymgr_reg2hw_reseed_interval_reg_t reseed_interval; // [405:390]
    keymgr_reg2hw_sw_binding_regwen_reg_t sw_binding_regwen; // [389:388]
    keymgr_reg2hw_sw_binding_mreg_t [3:0] sw_binding; // [387:260]
    keymgr_reg2hw_salt_mreg_t [3:0] salt; // [259:132]
    keymgr_reg2hw_key_version_mreg_t [0:0] key_version; // [131:100]
    keymgr_reg2hw_max_creator_key_ver_reg_t max_creator_key_ver; // [99:68]
    keymgr_reg2hw_max_owner_int_key_ver_reg_t max_owner_int_key_ver; // [67:36]
    keymgr_reg2hw_max_owner_key_ver_reg_t max_owner_key_ver; // [35:4]
    keymgr_reg2hw_err_code_reg_t err_code; // [3:0]
  } keymgr_reg2hw_t;

  ///////////////////////////////////////
  // Internal design logic to register //
  ///////////////////////////////////////
  typedef struct packed {
    keymgr_hw2reg_intr_state_reg_t intr_state; // [548:547]
    keymgr_hw2reg_cfg_regwen_reg_t cfg_regwen; // [546:546]
    keymgr_hw2reg_control_reg_t control; // [545:544]
    keymgr_hw2reg_sw_binding_regwen_reg_t sw_binding_regwen; // [543:543]
    keymgr_hw2reg_sw_share0_output_mreg_t [7:0] sw_share0_output; // [542:279]
    keymgr_hw2reg_sw_share1_output_mreg_t [7:0] sw_share1_output; // [278:15]
    keymgr_hw2reg_working_state_reg_t working_state; // [14:11]
    keymgr_hw2reg_op_status_reg_t op_status; // [10:8]
    keymgr_hw2reg_err_code_reg_t err_code; // [7:0]
  } keymgr_hw2reg_t;

  // Register Address
  parameter logic [BlockAw-1:0] KEYMGR_INTR_STATE_OFFSET = 8'h 0;
  parameter logic [BlockAw-1:0] KEYMGR_INTR_ENABLE_OFFSET = 8'h 4;
  parameter logic [BlockAw-1:0] KEYMGR_INTR_TEST_OFFSET = 8'h 8;
  parameter logic [BlockAw-1:0] KEYMGR_ALERT_TEST_OFFSET = 8'h c;
  parameter logic [BlockAw-1:0] KEYMGR_CFG_REGWEN_OFFSET = 8'h 10;
  parameter logic [BlockAw-1:0] KEYMGR_CONTROL_OFFSET = 8'h 14;
  parameter logic [BlockAw-1:0] KEYMGR_SIDELOAD_CLEAR_OFFSET = 8'h 18;
  parameter logic [BlockAw-1:0] KEYMGR_RESEED_INTERVAL_OFFSET = 8'h 1c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_BINDING_REGWEN_OFFSET = 8'h 20;
  parameter logic [BlockAw-1:0] KEYMGR_SW_BINDING_0_OFFSET = 8'h 24;
  parameter logic [BlockAw-1:0] KEYMGR_SW_BINDING_1_OFFSET = 8'h 28;
  parameter logic [BlockAw-1:0] KEYMGR_SW_BINDING_2_OFFSET = 8'h 2c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_BINDING_3_OFFSET = 8'h 30;
  parameter logic [BlockAw-1:0] KEYMGR_SALT_0_OFFSET = 8'h 34;
  parameter logic [BlockAw-1:0] KEYMGR_SALT_1_OFFSET = 8'h 38;
  parameter logic [BlockAw-1:0] KEYMGR_SALT_2_OFFSET = 8'h 3c;
  parameter logic [BlockAw-1:0] KEYMGR_SALT_3_OFFSET = 8'h 40;
  parameter logic [BlockAw-1:0] KEYMGR_KEY_VERSION_OFFSET = 8'h 44;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_CREATOR_KEY_VER_REGWEN_OFFSET = 8'h 48;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_CREATOR_KEY_VER_OFFSET = 8'h 4c;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_OWNER_INT_KEY_VER_REGWEN_OFFSET = 8'h 50;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_OWNER_INT_KEY_VER_OFFSET = 8'h 54;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_OWNER_KEY_VER_REGWEN_OFFSET = 8'h 58;
  parameter logic [BlockAw-1:0] KEYMGR_MAX_OWNER_KEY_VER_OFFSET = 8'h 5c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_0_OFFSET = 8'h 60;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_1_OFFSET = 8'h 64;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_2_OFFSET = 8'h 68;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_3_OFFSET = 8'h 6c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_4_OFFSET = 8'h 70;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_5_OFFSET = 8'h 74;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_6_OFFSET = 8'h 78;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE0_OUTPUT_7_OFFSET = 8'h 7c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_0_OFFSET = 8'h 80;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_1_OFFSET = 8'h 84;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_2_OFFSET = 8'h 88;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_3_OFFSET = 8'h 8c;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_4_OFFSET = 8'h 90;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_5_OFFSET = 8'h 94;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_6_OFFSET = 8'h 98;
  parameter logic [BlockAw-1:0] KEYMGR_SW_SHARE1_OUTPUT_7_OFFSET = 8'h 9c;
  parameter logic [BlockAw-1:0] KEYMGR_WORKING_STATE_OFFSET = 8'h a0;
  parameter logic [BlockAw-1:0] KEYMGR_OP_STATUS_OFFSET = 8'h a4;
  parameter logic [BlockAw-1:0] KEYMGR_ERR_CODE_OFFSET = 8'h a8;

  // Reset values for hwext registers
  parameter logic [0:0] KEYMGR_INTR_TEST_RESVAL = 1'h 0;
  parameter logic [1:0] KEYMGR_ALERT_TEST_RESVAL = 2'h 0;
  parameter logic [0:0] KEYMGR_CFG_REGWEN_RESVAL = 1'h 1;
  parameter logic [0:0] KEYMGR_SW_BINDING_REGWEN_RESVAL = 1'h 1;

  // Register Index
  typedef enum int {
    KEYMGR_INTR_STATE,
    KEYMGR_INTR_ENABLE,
    KEYMGR_INTR_TEST,
    KEYMGR_ALERT_TEST,
    KEYMGR_CFG_REGWEN,
    KEYMGR_CONTROL,
    KEYMGR_SIDELOAD_CLEAR,
    KEYMGR_RESEED_INTERVAL,
    KEYMGR_SW_BINDING_REGWEN,
    KEYMGR_SW_BINDING_0,
    KEYMGR_SW_BINDING_1,
    KEYMGR_SW_BINDING_2,
    KEYMGR_SW_BINDING_3,
    KEYMGR_SALT_0,
    KEYMGR_SALT_1,
    KEYMGR_SALT_2,
    KEYMGR_SALT_3,
    KEYMGR_KEY_VERSION,
    KEYMGR_MAX_CREATOR_KEY_VER_REGWEN,
    KEYMGR_MAX_CREATOR_KEY_VER,
    KEYMGR_MAX_OWNER_INT_KEY_VER_REGWEN,
    KEYMGR_MAX_OWNER_INT_KEY_VER,
    KEYMGR_MAX_OWNER_KEY_VER_REGWEN,
    KEYMGR_MAX_OWNER_KEY_VER,
    KEYMGR_SW_SHARE0_OUTPUT_0,
    KEYMGR_SW_SHARE0_OUTPUT_1,
    KEYMGR_SW_SHARE0_OUTPUT_2,
    KEYMGR_SW_SHARE0_OUTPUT_3,
    KEYMGR_SW_SHARE0_OUTPUT_4,
    KEYMGR_SW_SHARE0_OUTPUT_5,
    KEYMGR_SW_SHARE0_OUTPUT_6,
    KEYMGR_SW_SHARE0_OUTPUT_7,
    KEYMGR_SW_SHARE1_OUTPUT_0,
    KEYMGR_SW_SHARE1_OUTPUT_1,
    KEYMGR_SW_SHARE1_OUTPUT_2,
    KEYMGR_SW_SHARE1_OUTPUT_3,
    KEYMGR_SW_SHARE1_OUTPUT_4,
    KEYMGR_SW_SHARE1_OUTPUT_5,
    KEYMGR_SW_SHARE1_OUTPUT_6,
    KEYMGR_SW_SHARE1_OUTPUT_7,
    KEYMGR_WORKING_STATE,
    KEYMGR_OP_STATUS,
    KEYMGR_ERR_CODE
  } keymgr_id_e;

  // Register width information to check illegal writes
  parameter logic [3:0] KEYMGR_PERMIT [43] = '{
    4'b 0001, // index[ 0] KEYMGR_INTR_STATE
    4'b 0001, // index[ 1] KEYMGR_INTR_ENABLE
    4'b 0001, // index[ 2] KEYMGR_INTR_TEST
    4'b 0001, // index[ 3] KEYMGR_ALERT_TEST
    4'b 0001, // index[ 4] KEYMGR_CFG_REGWEN
    4'b 0011, // index[ 5] KEYMGR_CONTROL
    4'b 0001, // index[ 6] KEYMGR_SIDELOAD_CLEAR
    4'b 0011, // index[ 7] KEYMGR_RESEED_INTERVAL
    4'b 0001, // index[ 8] KEYMGR_SW_BINDING_REGWEN
    4'b 1111, // index[ 9] KEYMGR_SW_BINDING_0
    4'b 1111, // index[10] KEYMGR_SW_BINDING_1
    4'b 1111, // index[11] KEYMGR_SW_BINDING_2
    4'b 1111, // index[12] KEYMGR_SW_BINDING_3
    4'b 1111, // index[13] KEYMGR_SALT_0
    4'b 1111, // index[14] KEYMGR_SALT_1
    4'b 1111, // index[15] KEYMGR_SALT_2
    4'b 1111, // index[16] KEYMGR_SALT_3
    4'b 1111, // index[17] KEYMGR_KEY_VERSION
    4'b 0001, // index[18] KEYMGR_MAX_CREATOR_KEY_VER_REGWEN
    4'b 1111, // index[19] KEYMGR_MAX_CREATOR_KEY_VER
    4'b 0001, // index[20] KEYMGR_MAX_OWNER_INT_KEY_VER_REGWEN
    4'b 1111, // index[21] KEYMGR_MAX_OWNER_INT_KEY_VER
    4'b 0001, // index[22] KEYMGR_MAX_OWNER_KEY_VER_REGWEN
    4'b 1111, // index[23] KEYMGR_MAX_OWNER_KEY_VER
    4'b 1111, // index[24] KEYMGR_SW_SHARE0_OUTPUT_0
    4'b 1111, // index[25] KEYMGR_SW_SHARE0_OUTPUT_1
    4'b 1111, // index[26] KEYMGR_SW_SHARE0_OUTPUT_2
    4'b 1111, // index[27] KEYMGR_SW_SHARE0_OUTPUT_3
    4'b 1111, // index[28] KEYMGR_SW_SHARE0_OUTPUT_4
    4'b 1111, // index[29] KEYMGR_SW_SHARE0_OUTPUT_5
    4'b 1111, // index[30] KEYMGR_SW_SHARE0_OUTPUT_6
    4'b 1111, // index[31] KEYMGR_SW_SHARE0_OUTPUT_7
    4'b 1111, // index[32] KEYMGR_SW_SHARE1_OUTPUT_0
    4'b 1111, // index[33] KEYMGR_SW_SHARE1_OUTPUT_1
    4'b 1111, // index[34] KEYMGR_SW_SHARE1_OUTPUT_2
    4'b 1111, // index[35] KEYMGR_SW_SHARE1_OUTPUT_3
    4'b 1111, // index[36] KEYMGR_SW_SHARE1_OUTPUT_4
    4'b 1111, // index[37] KEYMGR_SW_SHARE1_OUTPUT_5
    4'b 1111, // index[38] KEYMGR_SW_SHARE1_OUTPUT_6
    4'b 1111, // index[39] KEYMGR_SW_SHARE1_OUTPUT_7
    4'b 0001, // index[40] KEYMGR_WORKING_STATE
    4'b 0001, // index[41] KEYMGR_OP_STATUS
    4'b 0001  // index[42] KEYMGR_ERR_CODE
  };
endpackage

