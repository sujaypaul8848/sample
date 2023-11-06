from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo2/__init__.py
from demo2 import __version__ as version

setup(
	name="demo2",
	version=version,
	description="Custom api fetching",
	author="sujay paul",
	author_email="sujay.paul@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
