#!/usr/bin/python

import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()


setuptools.setup(
	name='riptide',
	version='2.0.1', 
	description='Reaction Inclusion by Parsimony and Transcript Distribution (RIPTiDe)',
	author='Matthew Jenior',
	author_email='mattjenior@gmail.com',
	url='https://github.com/mjenior/riptide',
	packages=setuptools.find_packages(),
    install_requires=['cobra','symengine','pandas'],
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=long_description,
	)
