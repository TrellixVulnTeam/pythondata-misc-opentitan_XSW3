import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8512"
version_tuple = (0, 0, 8512)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8512")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8400"
data_version_tuple = (0, 0, 8400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8400")
except ImportError:
    pass
data_git_hash = "39ac4e2ecdd6e0a33a70e4ada24831a0d6d3aba8"
data_git_describe = "v0.0-8400-g39ac4e2ec"
data_git_msg = """\
commit 39ac4e2ecdd6e0a33a70e4ada24831a0d6d3aba8
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 28 15:18:49 2021 -0700

    [dv/alert_check] Fix tl_intg_err regression failure
    
    Alert auto response sequence should be triggered after dut_init is done,
    otherwise init process might count as signal integrity errors in
    alert_receiver_driver.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
