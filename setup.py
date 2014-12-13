# -*- coding: utf-8 -*-

# python std lib
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()
with open('docs/CHANGES') as f:
    history = f.read()

setup(
    name="mpcapi",
    version="0.1.0",
    description="API binding for Media Player Classic (MPC-HC)",
    long_description=readme + '\n\n' + history,
    author="Johan Andersson",
    author_email="Grokzen@gmail.com",
    maintainer='Johan Andersson',
    maintainer_email='Grokzen@gmail.com',
    packages=["mpcapi"],
    url='http://github.com/grokzen/mpcapi',
    license='MIT',
    install_requires=[
        'requests==2.5.0'
    ],
    keywords=[
        'mpc-hc',
        'api',
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    )
)
