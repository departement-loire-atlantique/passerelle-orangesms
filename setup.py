#! /usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import re
import subprocess
import sys

from setuptools.command.install_lib import install_lib as _install_lib
from setuptools.command.install import _install
from distutils.command.build import build as _build
from distutils.cmd import Command
from setuptools import setup, find_packages

class PostInstallCommand(_install):
    """Post-installation for installation mode. Activate plugin for passerelle"""
    def run(self):
        if os.path.exists('/etc/passerelle/settings.d'):
	    with open('/etc/passerelle/settings.d/passerelle-orangesms.py', 'w+') as f:
	        f.write("if 'passerelle_orangesms' not in INSTALLED_APPS:\n")
		f.write("  INSTALLED_APPS += ('passerelle_orangesms',)\n")
		f.write("  TENANT_APPS += ('passerelle_orangesms',)")
        _install.run(self)

def get_version():
    if os.path.exists('VERSION'):
        version_file = open('VERSION', 'r')
        version = version_file.read()
        version_file.close()
        return version
    if os.path.exists('.git'):
        p = subprocess.Popen(['git', 'describe', '--dirty', '--match=v*'], stdout=subprocess.PIPE)
        result = p.communicate()[0]
        if p.returncode == 0:
            version = result.split()[0][1:]
            return version
    return '0'

setup(
    name='passerelle-orangesms',
    version=get_version(),
    author='Julien Bayle <julien.bayle@loire-atlantique.fr>, Guillaume Gautier <guillaume.gautier@loire-atlantique.fr>',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/departement-loire-atlantique/passerelle-orangesms',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires=['django >= 1.8, <1.12',],
    zip_safe=False,
    cmdclass={
        'build': _build,
	'install_lib': _install_lib,
	'install': PostInstallCommand,
    }
)
