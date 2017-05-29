# -*- coding: utf-8 -*-

"""Floodgate parser module for player list."""

# Imports
from bs4 import BeautifulSoup as bs
from typing import List


class FgPlayer:
    """Floodgate player definition class."""

    def __init__(self, row: bs) -> None:
        """Parse Floodgate player table row to FgPlayer instance.

        @param row: row html
        """
        ths = row.find_all("th")
        self._name = ths[0].contents[0]
        self._games = int(ths[1].contents[0])
        self._rate = float(ths[2].contents[0])

    def get_name(self) -> str:
        """Get player name."""
        return self._name

    def get_games(self) -> int:
        """Get number of games."""
        return self._games

    def get_rate(self) -> float:
        """Get player rate."""
        return self._rate


def parse(html: str) -> List[FgPlayer]:
    """Parse player list html data.

    @param html: recent log html decode as str
    @return : list of floodgamte player
    """
    soup = bs(html)
    fg_table_list = soup.find_all("table")
    # get 2nd table and exclude header
    players = fg_table_list[1].find_all("tr")[1:]
    return [FgPlayer(row) for row in players]
