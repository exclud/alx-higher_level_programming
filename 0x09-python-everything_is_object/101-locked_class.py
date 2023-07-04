#!/usr/bin/python3
"""Define class Locked Class"""
from typing import Any


class LockedClass:
    """Prevent User from dynamically creating new instance
    """
    __slots__ = ('first_name', )
