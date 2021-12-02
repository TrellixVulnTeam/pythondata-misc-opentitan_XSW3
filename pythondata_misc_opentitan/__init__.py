import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8952"
version_tuple = (0, 0, 8952)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8952")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8840"
data_version_tuple = (0, 0, 8840)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8840")
except ImportError:
    pass
data_git_hash = "c6213a373d5da9d798903560e94f43f937b4e36f"
data_git_describe = "v0.0-8840-gc6213a373"
data_git_msg = """\
commit c6213a373d5da9d798903560e94f43f937b4e36f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Dec 1 15:01:30 2021 +0000

    [rom_ctrl] Check TL command integrity in ROM adapter
    
    This fixes the rom_ctrl_tl_intg_err test (where we weren't previously
    spotting malformed TL commands sent to the ROM).
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
