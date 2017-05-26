# -*- coding: utf-8 -*-

"""Exception definitions of Floodgate parser."""


class FgParseException(Exception):
    """Base exception raised for errors on Floodgate Parse."""

    pass


class FgInvalidSectionException(FgParseException):
    """Exception raised for errors of invalid content."""

    pass
