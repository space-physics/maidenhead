#!/usr/bin/env python
install_requires = []
tests_require =['pytest','nose','coveralls']

from setuptools import setup,find_packages

setup(name = "maidenhead",
    packages = find_packages(),
    version = "1.1.3",
    description = "Maidenhead Locator",
    long_description=open('README.rst').read(),
    author = ['Michael Hirsch',"Henri Kuiper"],
	  url = "https://github.com/scivision/maidenhead",
    keywords = ["location", "maidenhead"],
    classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 2.7", 
    "Programming Language :: Python :: 3.6", 
    "Programming Language :: Python :: 3.7", 
    'Topic :: Scientific/Engineering :: GIS',
        ],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests':tests_require},
    python_requires='>=2.7',
    scripts=['Maidenhead.py'],
)
