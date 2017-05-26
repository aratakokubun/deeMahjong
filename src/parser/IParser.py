# -*- coding: utf-8 -*-

"""Parsing data interface module."""

# Imports
from abc import ABCMeta, abstractmethod


class IParser(metaclass=ABCMeta):
    """Interface for data parser."""

    @abstractmethod
    def __parse__(self, rawdata: str):
        """Parse string data.

        @param rawdata: data to be parsed
        """
        pass
