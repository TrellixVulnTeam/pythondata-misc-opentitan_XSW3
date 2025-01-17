import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15043"
version_tuple = (0, 0, 15043)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15043")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14901"
data_version_tuple = (0, 0, 14901)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14901")
except ImportError:
    pass
data_git_hash = "2e9aec59cd5cc575ab562184f9d7d10553d9d9d0"
data_git_describe = "v0.0-14901-g2e9aec59cd"
data_git_msg = """\
commit 2e9aec59cd5cc575ab562184f9d7d10553d9d9d0
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Oct 28 15:51:44 2022 -0700

    [top-level] Add CSRNG command header builder.
    
    This commits adds a CSRNG command header function to switch to a more
    consistent command generation interface across top-level test cases.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
