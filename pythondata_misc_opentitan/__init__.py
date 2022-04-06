import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11411"
version_tuple = (0, 0, 11411)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11411")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11285"
data_version_tuple = (0, 0, 11285)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11285")
except ImportError:
    pass
data_git_hash = "1c943840c6d489c8250deae8144d369ceb2c60e4"
data_git_describe = "v0.0-11285-g1c943840c"
data_git_msg = """\
commit 1c943840c6d489c8250deae8144d369ceb2c60e4
Author: Weicai Yang <weicai@google.com>
Date:   Wed Mar 30 17:32:49 2022 -0700

    [top, dv] Update keymgr key derivation test
    
    1. added generating identity and SW data as well as checking them at SV
    2. added generating sideload key for all interfaces and check them via
       backdoor
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
