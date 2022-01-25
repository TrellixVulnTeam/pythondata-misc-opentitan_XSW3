import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9772"
version_tuple = (0, 0, 9772)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9772")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9650"
data_version_tuple = (0, 0, 9650)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9650")
except ImportError:
    pass
data_git_hash = "4db9450e5d9b92a3c4c6020fba4f9fb639d79423"
data_git_describe = "v0.0-9650-g4db9450e5"
data_git_msg = """\
commit 4db9450e5d9b92a3c4c6020fba4f9fb639d79423
Author: Igor Kouznetsov <igor.kouznetsov@wdc.com>
Date:   Tue Jan 18 14:12:12 2022 -0800

    [i2c, rtl] Removed SDA toggling when sending multiple bits of "1"s.
    
    Signed-off-by: Igor Kouznetsov <igor.kouznetsov@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
