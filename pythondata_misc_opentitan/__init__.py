import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14438"
version_tuple = (0, 0, 14438)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14438")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14296"
data_version_tuple = (0, 0, 14296)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14296")
except ImportError:
    pass
data_git_hash = "fcefd065d4c444f090b42534cd19d7511950f538"
data_git_describe = "v0.0-14296-gfcefd065d4"
data_git_msg = """\
commit fcefd065d4c444f090b42534cd19d7511950f538
Author: Weicai Yang <weicai@google.com>
Date:   Fri Sep 23 16:19:27 2022 -0700

    [spi_device/dv] Update TPM sequences
    
    1. Update locality sequence to use the new method
    2. Remove csb_consecutive and clean up used task/functions
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
