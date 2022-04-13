import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11556"
version_tuple = (0, 0, 11556)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11556")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11430"
data_version_tuple = (0, 0, 11430)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11430")
except ImportError:
    pass
data_git_hash = "e228d1257b7b83cadf3add722a695984c217f438"
data_git_describe = "v0.0-11430-ge228d1257"
data_git_msg = """\
commit e228d1257b7b83cadf3add722a695984c217f438
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Apr 12 05:21:23 2022 -0700

    [aes/dv] updated aes refines for V2
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
