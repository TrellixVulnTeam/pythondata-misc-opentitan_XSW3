import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10012"
version_tuple = (0, 0, 10012)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10012")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9888"
data_version_tuple = (0, 0, 9888)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9888")
except ImportError:
    pass
data_git_hash = "91ceb766586bc98892ba8cf0cbe2aae9a13caa28"
data_git_describe = "v0.0-9888-g91ceb7665"
data_git_msg = """\
commit 91ceb766586bc98892ba8cf0cbe2aae9a13caa28
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Feb 1 14:48:07 2022 -0500

    [sw/silicon_creator] Harden remaining lc_state switches
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
