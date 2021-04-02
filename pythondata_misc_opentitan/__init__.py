import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5683"
version_tuple = (0, 0, 5683)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5683")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5588"
data_version_tuple = (0, 0, 5588)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5588")
except ImportError:
    pass
data_git_hash = "76eb883ebbb734764bf81f8531d02f1aa9f207f0"
data_git_describe = "v0.0-5588-g76eb883eb"
data_git_msg = """\
commit 76eb883ebbb734764bf81f8531d02f1aa9f207f0
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 25 16:49:58 2021 -0700

    [top] Auto generate files
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
