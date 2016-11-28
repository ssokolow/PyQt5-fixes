#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='PyQt5_fixes',
    version='0.1.dev1',
    description='Workarounds for PyQt5 warts which I find myself using in '
                'multiple projects',
    author='Stephan Sokolow',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
    ],
    keywords='pyqt pyqt5 helpers fixes',
    packages=find_packages(exclude=['build', 'dist', 'docs', 'tests']),
    extras_require={
        'xdg_icons': ['PyXDG'],
    },
)
