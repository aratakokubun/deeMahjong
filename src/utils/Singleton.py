# -*- coding: utf-8 -*-

"""Singleton utility module."""


class Singleton(object):
    """Singleton module for python.

    Extends class object to implement a Singleton class.
    """

    __instance = None

    def __new__(cls, *args: str, **keys: str) -> 'Singleton':
        """Get singleton instance of this class."""
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
