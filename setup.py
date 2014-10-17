import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='pqaut',
    version='0.2.5',
    author='Gary Johnson',
    author_email = 'gary@gjtt.com',
    description = 'Automation for BDD testing PyQt apps',
    install_requires=['bottle'],
    tests_require=['bottle'],
    license = 'MIT License',
    packages = ['pqaut', 'pqaut.automator'],
    )
