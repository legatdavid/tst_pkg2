# Databricks notebook source
from setuptools import setup

# Add install requirements
setup(
    author="legatdavid",
    description="Testing DBC libraries",
    name="tst_pkg2",
    packages=find_packages(include=["tst_pkg2", "tst_pkg2.*"]),
    version="0.1.0",
    install_requires=['numpy'],
    python_requires=">=3.5",
)
