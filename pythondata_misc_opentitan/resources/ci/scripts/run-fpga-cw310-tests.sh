#!/bin/bash
# Copyright lowRISC contributors.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

set -x
set -e

. util/build_consts.sh

SHA=$(git rev-parse HEAD)
readonly SHA

# Copy bitstreams and related files into the cache directory so Bazel will have
# the corresponding targets in the @bitstreams workspace.
#
# TODO(#13807) Update this when we change the naming scheme.
readonly BIT_CACHE_DIR="${HOME}/.cache/opentitan-bitstreams/cache/${SHA}"
readonly BIT_SRC_DIR="${BIN_DIR}/hw/top_earlgrey"
readonly BIT_NAME_PREFIX="lowrisc_systems_chip_earlgrey_cw310_0.1.bit"
mkdir -p "${BIT_CACHE_DIR}"
cp "${BIT_SRC_DIR}/${BIT_NAME_PREFIX}.orig" \
    "${BIT_SRC_DIR}/${BIT_NAME_PREFIX}.splice" \
    "${BIT_SRC_DIR}/otp.mmi"  \
    "${BIT_SRC_DIR}/rom.mmi" \
    "${BIT_CACHE_DIR}"

echo -n "$SHA" > "${BIT_CACHE_DIR}/../../latest.txt"
export BITSTREAM="--offline --list ${SHA}"

# We will lose serial access when we reboot, but if tests fail we should reboot
# in case we've crashed the UART handler on the CW310's SAM3U
trap 'ci/bazelisk.sh run //sw/host/opentitantool -- --interface=cw310 fpga reset' EXIT

cw310_tags=( "cw310_test_rom" "cw310_rom" )
for tag in "${cw310_tags[@]}"; do
    ./bazelisk.sh query 'rdeps(//..., @bitstreams//...)' |
        xargs ci/bazelisk.sh test \
            --define DISABLE_VERILATOR_BUILD=true \
            --nokeep_going \
            --test_tag_filters="${tag}",-broken,-manual \
            --test_timeout_filters=short,moderate \
            --test_output=all \
            --build_tests_only \
            --define cw310=lowrisc \
            --flaky_test_attempts=2
done
