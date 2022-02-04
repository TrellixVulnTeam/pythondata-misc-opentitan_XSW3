import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10082"
version_tuple = (0, 0, 10082)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10082")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9958"
data_version_tuple = (0, 0, 9958)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9958")
except ImportError:
    pass
data_git_hash = "ca6dabfa85d0c8702f9d99f057a3778fb96f2637"
data_git_describe = "v0.0-9958-gca6dabfa8"
data_git_msg = """\
commit ca6dabfa85d0c8702f9d99f057a3778fb96f2637
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Jan 17 14:57:46 2022 -0800

    [csrng/rtl] d2s review updates
    
    RTL and documentation updates based on D2S review feedback.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>
    
    [csrng/rtl] D2S review items update
    
    Based on feedback from the D2S review, several items were updated
    in the PR for the csrng entropy block.
    See #10095 for details.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
