# -*- coding: utf-8 -*-

"""Config class module for database settings."""

# imports
import configparser

# Class definition


class FloodgateConfig:
    """Config class to read database configuration."""

    # Class constants
    DATABASE_KEY = "Database"
    PATH_KEY = "path"

    def __init__(self, config_path: str) -> None:
        """
        Read config file on construct.

        @param config_path: config file path
        """
        self._config = configparser.ConfigParser()
        self._config.read(config_path)

        self._db_path = self._config.get(
            self.DATABASE_KEY, self.PATH_KEY)

    @property
    def db_path(self) -> str:
        """I'm the 'db_path' property."""
        return self._db_path
