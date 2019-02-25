"""Little helper application to improve django choices (for fields)"""
from __future__ import unicode_literals
import pkg_resources
from os import path
from setuptools.config import read_configuration

from .choices import Choices, OrderedChoices, AutoDisplayChoices, AutoChoices  # noqa: F401


def _extract_version(package_name):
    try:
        # if package is installed
        version = pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        # if not installed, so we must be in source, with ``setup.cfg`` available
        _conf = read_configuration(path.join(
            path.dirname(__file__), '..', 'setup.cfg')
        )
        version = _conf['metadata']['version']

    return version


# '%s' % ... is a hack to ensure EXACT_VERSION is a unicode string in python 2,
# because pkg_resources.get_distribution(...).version returns a bytes str and
# that would fail when calling isnumeric() below. It can be safely removed when
# Python 2 support is removed.
EXACT_VERSION = '%s' % _extract_version('django_extended_choices')
VERSION = tuple(int(part) for part in EXACT_VERSION.split('.') if part.isnumeric())
