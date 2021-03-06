#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

import scdl

setup(
    name='scdl',
    version=scdl.__version__,
    packages=find_packages(),
    author="FlyinGrub",
    author_email="flyinggrub@gmail.com",
    description="Download Music from Souncloud",
    long_description=open('README.md').read(),
    install_requires=[
        'docopt',
        'soundcloud',
        'wget',
        'configparser',
        'mutagen'
    ],
    data_files=[
        (os.path.join(os.path.expanduser('~'), '.config/scdl'), ['config/scdl.cfg'])
    ],
    include_package_data=True,
    url='https://github.com/flyingrub/scdl',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    entry_points={
        'console_scripts': [
            'scdl = scdl.scdl:main',
        ],
    },
)
