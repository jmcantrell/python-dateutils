#!/usr/bin/env python

from setuptools import setup

setup(
        name='DateUtils',
        version='0.4.2',
        description='Various utilities for working with datetime objects.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            ],
        install_requires=[
            'ScriptUtils',
            'python-dateutil',
            'pytz'
            ],
        entry_points={
            'console_scripts': [
                'dateadd=dateadd:main',
                'datediff=datediff:main',
                ]
            },
        packages=[
            'dateutils',
            ],
        py_modules=[
            'dateadd',
            'datediff',
            ]
        )
