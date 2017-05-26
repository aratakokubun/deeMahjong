# -*- coding: utf-8 -*-

"""Config class module for floodgame."""

# imports
import configparser


# Class definition
class FloodgateConfig:
    """
    Config class to read floodgate mahjong server configuration.

    {@code: _url_server}: mahjong game server url
    {@code: _url_log_recent}: mjlog url of recent games
    {@code: _url_log_full}: mjlog url of all of the games
    {@code: _url_player}: player list url
    """

    # Class constants
    FLOODGATE_KEY = "Floodgate"
    URL_SERVER_KEY = "urlServer"
    URL_RECENT_KEY = "urlLogRecent"
    URL_FULL_KEY = "urlLogFull"
    URL_PLAYER_KEY = "urlPlayer"

    def __init__(self, config_path: str) -> None:
        """
        Read config file on construct.

        @param config_path: config file path
        """
        self._config = configparser.ConfigParser()
        self._config.read(config_path)

        self._url_server = self._config.get(
            self.FLOODGATE_KEY, self.URL_SERVER_KEY)
        self._url_log_recent = self._config.get(
            self.FLOODGATE_KEY, self.URL_RECENT_KEY)
        self._url_log_full = self._config.get(
            self.FLOODGATE_KEY, self.URL_FULL_KEY)
        self._url_player = self._config.get(
            self.FLOODGATE_KEY, self.URL_PLAYER_KEY)

    def get_url_server(self) -> str:
        """Get Url server string.

        @return server url
        """
        return self._url_server

    def get_url_log_recent(self) -> str:
        """Get Url log recent string.

        @return recent log url
        """
        return self._url_log_recent

    def get_url_log_full(self) -> str:
        """Get Url log full string.

        @return full log url
        """
        return self._url_log_full

    def get_url_player(self) -> str:
        """Get Url player string.

        @return player url
        """
        return self._url_player
