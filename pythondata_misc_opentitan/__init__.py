import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12411"
version_tuple = (0, 0, 12411)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12411")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12269"
data_version_tuple = (0, 0, 12269)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12269")
except ImportError:
    pass
data_git_hash = "bb1701c2872d1ee23e0b41a3e27d0a3c08174559"
data_git_describe = "v0.0-12269-gbb1701c28"
data_git_msg = """\
commit bb1701c2872d1ee23e0b41a3e27d0a3c08174559
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Apr 21 04:24:03 2022 -0700

    [dv,full_chip,pwrmgr] Add pwrmgr_sleep_power_glitch_reset test
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
