import os

from setuptools import find_namespace_packages, setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as reqs_file:
    requirements = reqs_file.read().splitlines()

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="warframe.py",
    author="Mettwasser",
    url="https://github.com/WFCD/warframe.py",
    description="An asynchronous Python API wrapper for the Warframestat API and (later) the warframe.market API.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    packages=find_namespace_packages(include=["warframe*"]),
    install_requires=requirements,
    license="MIT",
    python_requires=">=3.9.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Warframe API worldstate market wrapper",
)
