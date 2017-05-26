# -*- coding: utf-8 -*-

"""Floodgate parser utility function module."""

# Imports

# Constants
ERR_CONTENT = "エラー"

# Functions


def validate_content(content: str) -> bool:
    """Get if the content string is error or not.

    @param content: content string
    @return true: content is valid. <br>
            false: content is invalid.
    """
    return ERR_CONTENT in content
