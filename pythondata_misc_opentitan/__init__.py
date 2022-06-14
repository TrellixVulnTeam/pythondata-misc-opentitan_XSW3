import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12671"
version_tuple = (0, 0, 12671)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12671")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12529"
data_version_tuple = (0, 0, 12529)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12529")
except ImportError:
    pass
data_git_hash = "5003ad289b3cbb3fee7299db0a325d8749f163b0"
data_git_describe = "v0.0-12529-g5003ad289"
data_git_msg = """\
commit 5003ad289b3cbb3fee7299db0a325d8749f163b0
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Jun 10 15:20:13 2022 +0100

    [sigverify] Check OTBN instruction count.
    
    As an extra protection against fault injection attacks, check that the
    instruction count from the OTBN modexp routine falls within a feasible
    range given the control-flow paths available in the program.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
