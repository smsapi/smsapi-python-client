#!/usr/bin/env python

#         _/_/_/                              _/_/    _/_/_/    _/_/_/   
#      _/        _/_/_/  _/_/      _/_/_/  _/    _/  _/    _/    _/      
#       _/_/    _/    _/    _/  _/_/      _/_/_/_/  _/_/_/      _/       
#          _/  _/    _/    _/      _/_/  _/    _/  _/          _/        
#   _/_/_/    _/    _/    _/  _/_/_/    _/    _/  _/        _/_/_/  

import smsapi

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='smsapi-client',
    version=smsapi.__version__,
    description='Python client for manage SmsApi account.',
    long_description=open('README.md').read(),
    author='SMSAPI',
    author_email='bok@smsapi.pl',
    url='https://github.com/smsapi/python-client',
    packages=['smsapi', 'smsapi.actions'],
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'smsapi': 'smsapi'},
    include_package_data=True,
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Topic :: Communications :: Mobile messages'
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ),
    test_suite='tests.suite'
)