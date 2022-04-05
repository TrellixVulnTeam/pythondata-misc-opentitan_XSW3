import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11382"
version_tuple = (0, 0, 11382)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11382")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11256"
data_version_tuple = (0, 0, 11256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11256")
except ImportError:
    pass
data_git_hash = "81513e9ce92dfad11f374481f15a7db3659126ca"
data_git_describe = "v0.0-11256-g81513e9ce"
data_git_msg = """\
commit 81513e9ce92dfad11f374481f15a7db3659126ca
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Apr 4 14:36:16 2022 -0700

    [bazel] cleanup `verilator_params()` in `opentitan_functests()`
    
    The `verilator_params()` macro was refactored in a prior commit, but its
    invocations in `opentitan_functest()` rules were not. This cleans these
    up to remove un-needed (required) tags.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
