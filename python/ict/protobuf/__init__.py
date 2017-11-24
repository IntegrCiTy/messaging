import pkg_resources  # part of setuptools
try:
    __version__ = pkg_resources.require("ict-messaging")[0].version
except :
    pass
