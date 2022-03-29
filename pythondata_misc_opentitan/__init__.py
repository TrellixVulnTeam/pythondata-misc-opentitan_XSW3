import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11183"
version_tuple = (0, 0, 11183)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11183")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11057"
data_version_tuple = (0, 0, 11057)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11057")
except ImportError:
    pass
data_git_hash = "bdcaf1ea1633085271bb1a87c5cb568eb88af311"
data_git_describe = "v0.0-11057-gbdcaf1ea1"
data_git_msg = """\
commit bdcaf1ea1633085271bb1a87c5cb568eb88af311
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Mar 25 20:06:42 2022 +0000

    [dv,pwrmgr] sec cm testplan
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
