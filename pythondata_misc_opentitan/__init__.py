import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9369"
version_tuple = (0, 0, 9369)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9369")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9252"
data_version_tuple = (0, 0, 9252)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9252")
except ImportError:
    pass
data_git_hash = "464b15e6e07714a7f4a9d380a42dae97b8e6baf4"
data_git_describe = "v0.0-9252-g464b15e6e"
data_git_msg = """\
commit 464b15e6e07714a7f4a9d380a42dae97b8e6baf4
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jan 6 15:35:11 2022 -0800

    [dv] intg_err test cleanup and change passthru_mem_tl_intg_err to V2S
    
    Clean up some unused codes
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
