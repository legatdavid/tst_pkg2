# Databricks notebook source
from setuptools import setup

# Add install requirements
setup(
    author="legatdavid",
    description="Testing DBC libraries",
    name="tst_pkg2",
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas'],
    python_requires=">=3.5",
)
