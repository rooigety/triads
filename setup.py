# Copyright 2023 ROOIGETY, all rights reserved.
#
# Written by rooigety <flanker_sheen.Of@icloud.com> and originally
# created on 2023-03-13.

from setuptools import setup

PACKAGE_REQUIREMENTS = [
    "plotly",
    "streamlit",
    "typeguard",
]

# Local requirements.
LOCAL_REQUIREMENTS = []

# Include a fully-fledged testing framework.
TEST_REQUIREMENTS = [
    "coverage[toml]",
    "opencv-python",
    "pytest",
    "pytest-cov",
]

if __name__ == "__main__":
    setup(
        extras_require={"local": LOCAL_REQUIREMENTS, "test": TEST_REQUIREMENTS},
        install_requires=PACKAGE_REQUIREMENTS,
    )
