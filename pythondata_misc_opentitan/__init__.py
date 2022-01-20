import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9658"
version_tuple = (0, 0, 9658)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9658")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9536"
data_version_tuple = (0, 0, 9536)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9536")
except ImportError:
    pass
data_git_hash = "b81d0f4e362789b2b066f8b821c7eba2d48f0776"
data_git_describe = "v0.0-9536-gb81d0f4e3"
data_git_msg = """\
commit b81d0f4e362789b2b066f8b821c7eba2d48f0776
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jan 18 13:08:56 2022 -0800

    [dv/chip] reduce jtag_csr_rw runtime
    
    This PR reduces jtag_csr_rw runtime by choosing a subsets of csrs.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
