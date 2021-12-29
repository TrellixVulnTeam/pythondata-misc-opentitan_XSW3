import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9304"
version_tuple = (0, 0, 9304)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9304")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9187"
data_version_tuple = (0, 0, 9187)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9187")
except ImportError:
    pass
data_git_hash = "f3d772a52c4d32778f600124736468cd145524e1"
data_git_describe = "v0.0-9187-gf3d772a52"
data_git_msg = """\
commit f3d772a52c4d32778f600124736468cd145524e1
Author: Kosta Kojdic <kosta.kojdic@ensilica.com>
Date:   Tue Dec 28 20:37:14 2021 +0000

    Bit transfer, async fifo and abort
    
    Signed-off-by: Kosta Kojdic <kosta.kojdic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
