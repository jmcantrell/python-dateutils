#!/usr/bin/env python

from setuptools import setup

setup(

    name='dateutils',
    version='0.6.7',

    description='Various utilities for working with date and datetime objects',

    author='Jeremy Cantrell',
    author_email='jmcantrell@gmail.com',

    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
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
