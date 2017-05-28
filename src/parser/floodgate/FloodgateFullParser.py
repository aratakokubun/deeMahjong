# -*- coding: utf-8 -*-

"""Floodgate parser module for full log."""

# Imports
from bs4 import BeautifulSoup as bs
from src.parser.floodgate import FloodgateParser as fgparser
from typing import List


def parse(html: str, base_url: str) -> List[fgparser.FgGame]:
    """Parse full log html data.

    @param html: full log html decode as str
    @param base_url: url of src html
    @return : list of floodgamte games
    """
    soup = bs(html)
    fg_table_list = soup.find_all("table")
    # get 2nd table and exclude header
    games = fg_table_list[1].find_all("tr")[1:]
    return fgparser.parse_game_table(games, base_url)
