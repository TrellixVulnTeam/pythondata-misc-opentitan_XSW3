import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12799"
version_tuple = (0, 0, 12799)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12799")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12657"
data_version_tuple = (0, 0, 12657)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12657")
except ImportError:
    pass
data_git_hash = "6fa05ce5b92e8e1f7ab5bb9e99e635f2b9118a8d"
data_git_describe = "v0.0-12657-g6fa05ce5b9"
data_git_msg = """\
commit 6fa05ce5b92e8e1f7ab5bb9e99e635f2b9118a8d
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Jun 23 09:30:31 2022 +0100

    [otbn,dv] Tweak condition that dumps OTBN state in verilator sim
    
    This version ensures the final state (before secure wipe) gets dumped
    out on termination by an error as well as termination by ecall
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
