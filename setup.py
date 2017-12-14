#!/usr/bin/env python

from smsapi import version, name

from setuptools import setup, find_packages

setup(
    name=name,
    version=version,
    description='SmsAPI client',
    long_description=open('README.md').read(),
    author='SMSAPI',
    author_email='bok@smsapi.pl',
    url='https://github.com/smsapi/smsapi-python-client',
    packages=find_packages(),
    license=open('LICENSE').read(),
    install_requires=[
        'requests',
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
    test_suite='tests.suite'
)