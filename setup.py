#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


def main():
    description = 'A simple tool to apply role of ansible'

    setup(
        name='ansible-art',
        version='0.3.2',
        author='Tatsunori Saito',
        author_email='bbrfkr@gmail.com',
        url='https://github.com/bbrfkr/ansible-art',
        description=description,
        long_description=description,
        zip_safe=False,
        include_package_data=True,
        packages=['ansibleart'],
        package_dir={'ansibleart': 'ansibleart'},
        package_data={'ansibleart': ['data/*']},
        install_requires=[],
        scripts=['ansibleart/bin/ansible-art'],
        tests_require=[],
        setup_requires=[],
    )


if __name__ == '__main__':
    main()
