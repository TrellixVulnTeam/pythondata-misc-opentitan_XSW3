import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5217"
version_tuple = (0, 0, 5217)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5217")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5126"
data_version_tuple = (0, 0, 5126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5126")
except ImportError:
    pass
data_git_hash = "f3b61c03969b1dbe65357227bc4645463350a6ec"
data_git_describe = "v0.0-5126-gf3b61c039"
data_git_msg = """\
commit f3b61c03969b1dbe65357227bc4645463350a6ec
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Jan 14 21:34:25 2021 -0800

    [fpv] First update CSR assertion check
    
    This PR is a first update to FPV csr auto assertion checks.
    This PR uses an internal variable to store write value from SW and check
    the readout csr only if there is no hw write access to the register.
    Upcoming PRs will support more types of regs.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
