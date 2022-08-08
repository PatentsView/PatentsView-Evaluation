import pkg_resources

__version__ = pkg_resources.require("pv_evaluation")[0].version

__all__ = ["__version__"]
