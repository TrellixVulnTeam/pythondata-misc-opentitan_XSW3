import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11352"
version_tuple = (0, 0, 11352)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11352")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11226"
data_version_tuple = (0, 0, 11226)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11226")
except ImportError:
    pass
data_git_hash = "615579ef088d272354f6cd1df7c8f20642733dec"
data_git_describe = "v0.0-11226-g615579ef0"
data_git_msg = """\
commit 615579ef088d272354f6cd1df7c8f20642733dec
Author: Miguel Young de la Sota <mcyoung@google.com>
Date:   Thu Mar 31 14:34:51 2022 -0400

    [bazel] Migrate all linker scripts to use ld_library()
    
    Signed-off-by: Miguel Young de la Sota <mcyoung@google.com>

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
