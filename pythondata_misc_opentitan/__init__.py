import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14744"
version_tuple = (0, 0, 14744)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14744")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14602"
data_version_tuple = (0, 0, 14602)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14602")
except ImportError:
    pass
data_git_hash = "3861c8701d60558c707ae80d16fb5a7a4a634887"
data_git_describe = "v0.0-14602-g3861c8701d"
data_git_msg = """\
commit 3861c8701d60558c707ae80d16fb5a7a4a634887
Author: Miles Dai <milesdai@google.com>
Date:   Thu Oct 13 15:23:28 2022 -0400

    [ci/ottf] Mark the OTTF flow control test as broken
    
    Signed-off-by: Miles Dai <milesdai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
