from setuptools import setup, find_packages
import codecs
import os
import sys

VERSION = '0.0.3'
DESCRIPTION = 'Add, Multiply, Mod, Divide Large number'
LONG_DESCRIPTION = """
Calculation with very large number
"""

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

# Setting up
setup(
    name="infp",
    version=VERSION,
    author="Vu Diep",
    author_email="vudiep411@gmail.com",
    description=readme,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'data structure', 'math', 'big number', 'infinite precision'],
    
)