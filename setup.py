#!/usr/bin/env python
req = ['nose']

from setuptools import setup,find_packages

setup(name = "maidenhead",
    packages = find_packages(),
    version = "1.1.2",
    description = "Maidenhead Locator",
    author = ['Michael Hirsch',"Henri Kuiper"],
	url = "https://github.com/scivision/maidenhead",
    keywords = ["location", "maidenhead"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        ],
    install_requires=req,
    python_requires='>=2.7',
)
