# -*- coding: utf-8 -*-

"""Player table sqlalchemy definition."""

# imports
from sqlalchemy import Table, Column, Integer, String
from src.dao.DbMeta import DbMeta
from src.utils.Singleton import Singleton


class PlayerTable(Singleton):
    """Player Table singleton class."""

    # constants
    __TABLE_NAME = 'player'

    def __init__(self) -> None:
        """Init table metadata on construct."""
        self.__table = Table(
            self.__TABLE_NAME,
            DbMeta().db_path,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('rate', Integer)
        )
        self.__table.create(checkfirst=True)

    @property
    def table(self) -> Table:
        """I'm the 'table' property."""
        return self.__table
