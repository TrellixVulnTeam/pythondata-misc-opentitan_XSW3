import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15034"
version_tuple = (0, 0, 15034)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15034")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14892"
data_version_tuple = (0, 0, 14892)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14892")
except ImportError:
    pass
data_git_hash = "175e33f823e21781f368773083b097f4e7edd809"
data_git_describe = "v0.0-14892-g175e33f823"
data_git_msg = """\
commit 175e33f823e21781f368773083b097f4e7edd809
Author: Michael Schaffner <msf@google.com>
Date:   Thu Oct 27 20:03:08 2022 -0700

    [rv_dm] Add support for R/W errors
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
