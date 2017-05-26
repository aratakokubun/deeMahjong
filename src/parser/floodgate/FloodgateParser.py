# -*- coding: utf-8 -*-

"""Floodgate parser module.

You can use this module as a common util to parse floodgate mahjong web site.
"""

# Imports
from bs4 import BeautifulSoup as bs
import FloodgateParserUtils as fputils
import FloodgateParseExceptions as fpe
from typing import List


class FgGame:
    """Floodgate game definition class."""

    def __init__(self, row: bs, base_url: str) -> None:
        """Parse floodgate result table row.

        @param row: row html
        @param base_url: url of src html
        @throws FgInvalidSectionException: row data can not be parsed
        """
        if not fputils.validate_content(row.span.contents[0]):
            raise fpe.FgInvalidSectionException()

        self._time = row.td.contents[0]
        self._players = [td.contents[0] for td in row.find_all('td')[2:9:2]]
        self._url = base_url + row.a.attrs['href']

    def get_time(self) -> str:
        """Get game time.

        @return game time
        """
        return self._time

    def get_players(self) -> List[str]:
        """Get game players.

        @return game players, length 4
        """
        return self._players

    def get_url(self) -> str:
        """Get game log url.

        @return game log url
        """
        return self._url


def parse_game_table(table: List[bs], base_url: str) -> List[FgGame]:
    """Parse floodgate result table url.

    @param table: game table in html
    @param base_url: url of src html
    @return list of Floodgate games.
    """
    return [FgGame(row, base_url) for row in table]
