import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9300"
version_tuple = (0, 0, 9300)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9300")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9183"
data_version_tuple = (0, 0, 9183)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9183")
except ImportError:
    pass
data_git_hash = "c85ddf7af30f139984f109df07cf82b544c5ecba"
data_git_describe = "v0.0-9183-gc85ddf7af"
data_git_msg = """\
commit c85ddf7af30f139984f109df07cf82b544c5ecba
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Dec 28 10:53:15 2021 -0800

    [fpv/script] Clean up script
    
    1. Clean up alert_handler's counter abstraction path because
    alert_handler updated the counters to double_lsfr and prim_count.
    2. Clean up result parsing script to continue the parsing script even
    though there was coverage error. This can ensure we still have the
    assertion pass/fail results.
    3. Clean up port updates from rv_dm.
    4. Downgrade a pwrmgr's error to warning, as both xcelium and VCS did
    not report it as an error.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
