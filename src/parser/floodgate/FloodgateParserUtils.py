# -*- coding: utf-8 -*-

"""Floodgate parser utility function module."""

# Imports
from bs4 import BeautifulSoup as bs

# Constants
ERR_CONTENT = "Error"

# Functions


def validate_content(content: bs) -> bool:
    """Get if the content string is error or not.

    @param content: content row beautifulsoup
    @return true: content is valid. <br>
            false: content is invalid.
    """
    tds = content.find_all("td")
    if len(tds) < 2:
        return False
    else:
        return ERR_CONTENT not in str(tds[1].contents[0])
