from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path



VERSION = '1.0.1'
DESCRIPTION = 'dcfdfdfdf'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lalalaopti",
    version=VERSION,
    author="HW",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)