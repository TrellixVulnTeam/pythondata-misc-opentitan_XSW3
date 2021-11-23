import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8823"
version_tuple = (0, 0, 8823)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8823")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8711"
data_version_tuple = (0, 0, 8711)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8711")
except ImportError:
    pass
data_git_hash = "0e46b8a18740f38245b443726be059f4c05b896c"
data_git_describe = "v0.0-8711-g0e46b8a18"
data_git_msg = """\
commit 0e46b8a18740f38245b443726be059f4c05b896c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Nov 19 15:20:06 2021 -0800

    [dv/alert_handler] Randomize mubi input
    
    This PR randomize mubi-related input in alert_handler testbench
    regarding lpg. To randomize mubi enum type, we also disabled some
    assertions.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
