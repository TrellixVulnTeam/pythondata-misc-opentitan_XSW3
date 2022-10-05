import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14572"
version_tuple = (0, 0, 14572)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14572")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14430"
data_version_tuple = (0, 0, 14430)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14430")
except ImportError:
    pass
data_git_hash = "b4383c7e6756bb52290eda5d7ea7a3f70b68e663"
data_git_describe = "v0.0-14430-gb4383c7e67"
data_git_msg = """\
commit b4383c7e6756bb52290eda5d7ea7a3f70b68e663
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 5 13:39:13 2022 -0700

    [cleanup] Fix merge skew
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
