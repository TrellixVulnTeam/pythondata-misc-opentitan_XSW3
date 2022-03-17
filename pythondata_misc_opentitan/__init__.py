import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10939"
version_tuple = (0, 0, 10939)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10939")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10813"
data_version_tuple = (0, 0, 10813)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10813")
except ImportError:
    pass
data_git_hash = "5857c501eb04b8cbd1b90f5b146fb84e8b9d7e0b"
data_git_describe = "v0.0-10813-g5857c501e"
data_git_msg = """\
commit 5857c501eb04b8cbd1b90f5b146fb84e8b9d7e0b
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Mar 16 15:21:26 2022 -0700

    [dv/otp] sec_cm
    
    This PR update security countermeasure tasks:
    1). Update exp_status_val when injecting fault on DV
    2). After fault injected, this PR checks if otp is blocked by accessing
      the OTP.
    3). Disable assertions due to index OOB.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
