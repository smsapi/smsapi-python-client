#!/usr/bin/env python

from smsapi import version, name

from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name=name,
    version=version,
    description='SmsAPI client',
    author='SMSAPI',
    author_email='bok@smsapi.pl',
    url='https://github.com/smsapi/smsapi-python-client',
    packages=find_packages(exclude=["tests.*",  "tests"]),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
    test_suite='tests.suite',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
