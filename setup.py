# {dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl
#
# Durante el desarrollo:
#   pip install -e .
#
# Para generar el wheel
#   python setup.py bdist_wheel
#   pip install dist/MiniGameEngine-X.Y.Z-py3-none-any.whl

from setuptools import setup

SETUP = {
    "author": "Roberto Carrasco",
    "author_email": "titos.carrasco@gmail.com",
    "description": "Mini Game Engine",
    "license": "MIT",
    "maintainer": "Roberto Carrasco",
    "maintainer_email": "titos.carrasco@gmail.com",
    "name": "MiniGameEngine",
    "package_dir": {"": "src"},
    "packages": ["MiniGameEngine"],
    "version": "0.2.1",
}

setup(**SETUP)
