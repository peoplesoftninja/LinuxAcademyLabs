
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name = 'hr',
    version = 0.1.0,
    description = 'CLS User management Utility',
    long_description = readme,
    author = 'Szaidy',
    author_email = 'szaidy@gmail.com',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = []
    )

