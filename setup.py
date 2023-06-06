from setuptools import find_namespace_packages, setup


with open("requirements.txt") as reqs_file:
    requirements = reqs_file.readlines()

setup(
    name="pyframe",
    version="0.1.0",
    author="Mettwasser",
    url="https://github.com/Mettwasser/pyframe",
    description="An asynchronous Python API wrapper for the Warframestat API and (later) the warframe.market API.",
    packages=find_namespace_packages(include=["pyframe*"]),
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
