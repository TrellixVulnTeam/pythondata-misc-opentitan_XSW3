import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10756"
version_tuple = (0, 0, 10756)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10756")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10630"
data_version_tuple = (0, 0, 10630)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10630")
except ImportError:
    pass
data_git_hash = "ae67983f67cf343e1a233b325f5470c693439a2f"
data_git_describe = "v0.0-10630-gae67983f6"
data_git_msg = """\
commit ae67983f67cf343e1a233b325f5470c693439a2f
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Mar 3 16:42:01 2022 -0800

    [dv/rstmgr] Remove first_reset support in tests
    
    The RTL recently took out the rst_cpu_n input and associated
    functionality. Fix the reset test to match.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
