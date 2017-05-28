# -*- coding: utf-8 -*-

"""Floodgate parser module for recent log."""

# Imports
from bs4 import BeautifulSoup as bs
from src.parser.floodgate import FloodgateParser as fgparser
from typing import List


def parse(html: str, base_url: str) -> List[fgparser.FgGame]:
    """Parse recent log html data.

    @param html: recent log html decode as str
    @param base_url: url of src html
    @return : list of floodgamte games
    """
    soup = bs(html)
    fg_table_list = soup.find_all("table")
    # get 3rd table and exclude header
    games = fg_table_list[2].find_all("tr")[1:]
    return fgparser.parse_game_table(games, base_url)
