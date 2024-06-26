#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:${USER}
:Date  :${DATE} ${TIME}
"""
import pathlib

from youqu3._setting._setting import _Setting


class _Config(_Setting):
    """
    Application library configuration
    """
    ROOTDIR = pathlib.Path(__file__).absolute().parent


config = _Config()
