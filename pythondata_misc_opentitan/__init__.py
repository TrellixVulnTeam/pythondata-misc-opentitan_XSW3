import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8822"
version_tuple = (0, 0, 8822)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8822")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8710"
data_version_tuple = (0, 0, 8710)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8710")
except ImportError:
    pass
data_git_hash = "f080eec9b152f08cfd5b7ffb900eb29972de11c5"
data_git_describe = "v0.0-8710-gf080eec9b"
data_git_msg = """\
commit f080eec9b152f08cfd5b7ffb900eb29972de11c5
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Nov 10 17:47:09 2021 -0800

    [pwrmgr] Enhance pwrmgr escalation network check
    
    - Added timeout check to escalation network clock/resets
    - Fixes #8658
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
