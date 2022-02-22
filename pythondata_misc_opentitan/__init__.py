import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10463"
version_tuple = (0, 0, 10463)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10463")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10337"
data_version_tuple = (0, 0, 10337)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10337")
except ImportError:
    pass
data_git_hash = "61fe79cf053e6ef66aa60335de358d847566bd91"
data_git_describe = "v0.0-10337-g61fe79cf0"
data_git_msg = """\
commit 61fe79cf053e6ef66aa60335de358d847566bd91
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 21 23:43:34 2022 +0000

    Remove incorrect byte count from comment
    
    The 896 here is correct and matches a comment about scratchpad memory
    layout at the top of p384_verify.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
