"""Stormbreaker setup module."""

from setuptools import find_packages, setup


PACKAGE_NAME = "stormbreaker"

INSTALLATION_REQUIREMENTS = [
    "flask",
    "celery[redis]",
    "redis",
    "pymongo",
    "selenium",
]


setup(
    name=PACKAGE_NAME,
    packages=find_packages(include=[PACKAGE_NAME, PACKAGE_NAME + '.*']),
    include_package_data=True,
    install_requires=INSTALLATION_REQUIREMENTS,
)
