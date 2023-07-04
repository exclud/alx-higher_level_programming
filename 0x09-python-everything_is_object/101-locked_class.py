#!/usr/bin/python3
"""Define class Locked Class"""


class LockedClass:
    """
    Prevent User from dynamically creating new instance
    """
    __slots__ = ('first_name', )
