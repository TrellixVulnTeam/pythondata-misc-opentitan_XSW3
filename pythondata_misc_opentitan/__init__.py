import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11001"
version_tuple = (0, 0, 11001)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11001")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10875"
data_version_tuple = (0, 0, 10875)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10875")
except ImportError:
    pass
data_git_hash = "b8cdb2e1e6dff9f714963dcfd8f01d73cbc2cf2e"
data_git_describe = "v0.0-10875-gb8cdb2e1e"
data_git_msg = """\
commit b8cdb2e1e6dff9f714963dcfd8f01d73cbc2cf2e
Author: Nikola Miladinovic <nikola.miladinovic@ensilica.com>
Date:   Fri Mar 18 12:14:04 2022 +0000

    [flash_ctrl] Small fix for flash_erase_suspend test
    
    Fix of erase suspend test for creator and owner partition
    
    Signed-off-by: Nikola Miladinovic <nikola.miladinovic@ensilica.com>

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
