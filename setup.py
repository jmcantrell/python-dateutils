#!/usr/bin/env python

from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.mkd'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='dateutils',
    version='0.6.9',

    description='Various utilities for working with date and datetime objects',

    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Jeremy Cantrell',
    author_email='jmcantrell@gmail.com',
    url='https://github.com/jmcantrell/python-dateutils',

    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],

    install_requires=[
        'argparse',
        'python-dateutil',
        'pytz'
    ],

    entry_points={
        'console_scripts': [
            'dateadd = dateutils.dateadd:main',
            'datediff = dateutils.datediff:main',
        ],
    },

    packages=[
        'dateutils',
    ],

)
