import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13322"
version_tuple = (0, 0, 13322)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13322")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13180"
data_version_tuple = (0, 0, 13180)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13180")
except ImportError:
    pass
data_git_hash = "c1a79547494105265e2d04457a36659ab6142d62"
data_git_describe = "v0.0-13180-gc1a7954749"
data_git_msg = """\
commit c1a79547494105265e2d04457a36659ab6142d62
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jul 26 17:43:23 2022 -0700

    [utils,dvsim] Add wall-clock timeout feature
    
    Add a timeout for builds and runs. Set it in Modes, and enable overriding it
    via dvsim arguments.
    
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
