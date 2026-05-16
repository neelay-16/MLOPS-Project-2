from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mlops-project-2",
    version="0.1",
    author="Neelyaaaa",
    packages=find_packages(where="."),   # Explicit
    package_dir={"": "."},
    install_requires=requirements,
    python_requires=">=3.11",
)