import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10004"
version_tuple = (0, 0, 10004)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10004")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9880"
data_version_tuple = (0, 0, 9880)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9880")
except ImportError:
    pass
data_git_hash = "53100f7eacf76361493dbb744a98e6291d0ac748"
data_git_describe = "v0.0-9880-g53100f7ea"
data_git_msg = """\
commit 53100f7eacf76361493dbb744a98e6291d0ac748
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Jan 31 19:24:54 2022 -0800

    [flash_ctrl] Attempt to fix fpga loop inference part 3
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
