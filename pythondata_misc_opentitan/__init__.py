import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5655"
version_tuple = (0, 0, 5655)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5655")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5560"
data_version_tuple = (0, 0, 5560)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5560")
except ImportError:
    pass
data_git_hash = "39abe941ebe45d6673ebc522875b1274470e2b8f"
data_git_describe = "v0.0-5560-g39abe941e"
data_git_msg = """\
commit 39abe941ebe45d6673ebc522875b1274470e2b8f
Author: Weicai Yang <weicai@google.com>
Date:   Tue Mar 30 18:57:44 2021 -0700

    [spi_device/dv] Disable overflow assertion for overflow seq
    
    The overflow is intentional, disable the assertion check in RTL
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
