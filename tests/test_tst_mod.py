# Databricks notebook source
from .tst_mod import tst_func


def test_tst_func():
    assert tst_func() is True    # noqa: W391
