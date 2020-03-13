"""pip setup file for restgun"""
from setuptools import setup

with open("README.md", "r") as readme:
    DESC = readme.read()

setup(
    name="pygitcmd",
    version="1.0.0",
    author="Samuel Waugh",
    author_email="swwouf@hotmail.com",
    maintainer="Samuel Waugh",
    maintainer_email="swwouf@hotmail.com",
    description="Python Git wrapper using CMD instead of libgit2.",
    long_description=DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    packages=["pygitcmd"]
)
