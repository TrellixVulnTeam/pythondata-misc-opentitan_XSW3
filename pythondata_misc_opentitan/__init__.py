import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8800"
version_tuple = (0, 0, 8800)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8800")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8688"
data_version_tuple = (0, 0, 8688)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8688")
except ImportError:
    pass
data_git_hash = "802b8278acc101ed33b1c683ff6cabffea18de95"
data_git_describe = "v0.0-8688-g802b8278a"
data_git_msg = """\
commit 802b8278acc101ed33b1c683ff6cabffea18de95
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Nov 19 06:39:47 2021 -0800

    [entropy_src/doc] align otp input names
    
    The hjson refers to internal names, not the actual input names related to otp efuses.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
