import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8516"
version_tuple = (0, 0, 8516)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8516")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8404"
data_version_tuple = (0, 0, 8404)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8404")
except ImportError:
    pass
data_git_hash = "8712cd84e9e14ef83de91f08730f540d4185e2be"
data_git_describe = "v0.0-8404-g8712cd84e"
data_git_msg = """\
commit 8712cd84e9e14ef83de91f08730f540d4185e2be
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri Oct 22 11:54:51 2021 -0700

    [entropy_src/dv] Support single-bit rng mode
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
