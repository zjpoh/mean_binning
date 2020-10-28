"""
Mean binning setup.py

Created by referencing to https://github.com/pypa/sampleproject/blob/master/setup.py
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")
install_requires = [
    line for line in (here / "requirements.txt").read_text() if not line.startswith("#")
]
dev_requires = [
    "pytest",
    "coverage",
    "pylint",
    "flake8",
    "black",
    "isort",
]
VERSION = "0.1.0"

setup(
    name="mean_binning",
    version=VERSION,
    description="Binning recursively using mean value",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjpoh/mean_binning",
    author="zjpoh",
    classifiers=[  # Optional
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="data science, binning, histrogram",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires,
    },
    license="MIT",
)
