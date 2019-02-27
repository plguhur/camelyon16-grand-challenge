from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import shutil
import os


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='camelyon16',
    version='0.1',
    url='https://github.com/plguhur/camelyon16-grand-challenge/',
    long_description=readme(),
    zip_safe=False,
    include_package_data=True,
)
