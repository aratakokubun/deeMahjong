# -*- coding: utf-8 -*-

"""Database metadata module."""

# imports
from sqlalchemy import create_engine, MetaData
from src.utils.Singleton import Singleton
from src.config.DatabaseConf import DatabaseConf


class DbMeta(Singleton):
    """Database metadata singleton class."""

    # Constants
    __CONFIG_PATH = "config/db.conf"

    def __init__(self) -> None:
        """Init metadata on construct."""
        config = DatabaseConf(self.__CONFIG_PATH)
        db_path = config.db_path
        engine = create_engine(db_path, echo=True)
        self.__metadata = MetaData()
        self.__metadata.bind = engine

    @property
    def db_path(self) -> MetaData:
        """I'm the 'metadata' property."""
        return self.__metadata
