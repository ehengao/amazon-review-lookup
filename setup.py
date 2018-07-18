#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Devlopment setup: pip install -e .[dev]
Production setup: pip install .
Running Test: pytest
"""
import subprocess
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup
from setuptools.command.develop import develop

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

DEPENDENCY_LINKS = []
REQUIREMENT_DEV = []
REQUIREMENT = []

with open('requirements_dev.txt') as fd:
    for line in fd:
        line = line.rstrip()
        if 'git+ssh' in line or 'git+https' in line:
            pkg = line.split('#')[-1]
            DEPENDENCY_LINKS.append(line + '-0')
            REQUIREMENT_DEV.append(pkg.replace('egg=', ''))
        else:
            REQUIREMENT_DEV.append(line)

with open('requirements.txt') as fd:
    for line in fd:
        line = line.rstrip()
        if 'git+ssh' in line or 'git+https' in line:
            pkg = line.split('#')[-1]
            if line + '-0' not in DEPENDENCY_LINKS:
                DEPENDENCY_LINKS.append(line + '-0')
            REQUIREMENT.append(pkg.replace('egg=', ''))
        else:
            REQUIREMENT_DEV.append(line)


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        subprocess.run(
            ['git', 'config', 'alias.push-version', 'push origin --tags']
        )
        subprocess.run(['pre-commit', 'install'])


setup(
    name='amazon_review_lookup',
    version='0.0.1',
    description="Amazon Product bad reviews lookup",
    entry_points={
        'console_scripts': [
            'amazon-review-lookup=amazon_review_lookup.cli:main'
        ]
    },
    install_requires=REQUIREMENT,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='amazon_review_lookup, amazon-review-lookup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    test_suite='tests',
    tests_require=REQUIREMENT_DEV,
    dependency_links=DEPENDENCY_LINKS,
    url='https://github.com/ehengao/amazon-review-lookup',
    zip_safe=False,
    author="Heng GAO",
    author_email='heng.gao.us@gmail.com',
    cmdclass={'develop': PostDevelopCommand},
    extras_require={'dev': REQUIREMENT_DEV},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
