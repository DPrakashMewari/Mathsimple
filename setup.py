import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Simplesquare",
    version="0.0.1",
    description="It square the number",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DPrakashMewari/Mathsimple",
    author="Chandra Prakash Mewari",
    author_email="Prakash.mewari@yahoo.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages = ['Simplesquare'],
    include_package_data =True,
    install_requires = [],
    entry_points={
        "console_scripts":[
            "Simplesquare=Simplesquare.__main__:main",
            ]
    },
)