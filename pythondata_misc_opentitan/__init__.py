import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12636"
version_tuple = (0, 0, 12636)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12636")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12494"
data_version_tuple = (0, 0, 12494)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12494")
except ImportError:
    pass
data_git_hash = "41f33a8909e00c9137ad64ab3a459d1ccaff958c"
data_git_describe = "v0.0-12494-g41f33a890"
data_git_msg = """\
commit 41f33a8909e00c9137ad64ab3a459d1ccaff958c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jun 7 14:32:04 2022 -0700

    [rtl/alert_handler] Enhance alert_handler FSM for sec_cm
    
    This PR enhances alert_handler's FSM error output to avoid attackers
    continuously drive state_d or attack FSM and prim_counter/lfsr together.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
