from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
name = "MLOPS Project -2",
version = "0.1",
author = "Neelyaaaa",
packages=find_packages(),
install_requires = requirements,
)