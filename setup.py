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
    name='smsapi-pozytywnie',
    version=smsapi.__version__,
    description='Python library for manage SmsApi account via HTTP/S',
    author='SMSAPI',
    author_email='bok@smsapi.pl',
    url='https://github.com/Kern3l/smsapi-python-client',
    packages=['smsapi', 'smsapi.actions'],
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'smsapi': 'smsapi'},
    include_package_data=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
    test_suite='tests.suite'
)
