# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='python_simple_swiftclient',
    description='A simple Openstack Swift Client written in Python to manage swift objects using just python standard libraries.',
    url='https://github.com/hcltech-ssw/python-simple-swiftclient',
    version='0.0.3',
    author='HCLTech-SSW Team',
    author_email='hcl_ss_oss@hcl.com',
    packages=find_packages(),
    scripts=['bin/python-simple-swiftclient'],
)
