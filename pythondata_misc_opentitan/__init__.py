import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12430"
version_tuple = (0, 0, 12430)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12430")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12288"
data_version_tuple = (0, 0, 12288)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12288")
except ImportError:
    pass
data_git_hash = "15bc9e3527d89d793d2ca740403adad262f708ac"
data_git_describe = "v0.0-12288-g15bc9e352"
data_git_msg = """\
commit 15bc9e3527d89d793d2ca740403adad262f708ac
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue May 31 06:22:00 2022 -0700

    [adc_ctrl] Fix a few documentation / comment nits
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
