from setuptools import find_packages, setup

setup(
    name="Primera_Parte",
    packages=find_packages(exclude=["Primera_Parte_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
