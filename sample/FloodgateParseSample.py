# -*- coding: utf-8 -*-

"""Sample script use Floodgate parser."""

# Imports
import urllib.request

from src.parser.floodgate import FloodgateRecentParser as fgrparser
from src.parser.floodgate import FloodgateFullParser as fgfparser
from src.config import FloodgateConfig as fgconfig

if __name__ == "__main__":
    config = fgconfig.FloodgateConfig("../config/parser.conf")

    html_recent = urllib.request.urlopen(config.get_url_log_recent()).read()
    fggame_list = fgrparser.parse(html_recent.decode(
        "utf-8"), base_url=config.get_url_log_recent())
    print("1st element in recent " + str(len(fggame_list)) + ": " +
          fggame_list[0].get_time() + ": " + fggame_list[0].get_url())

    html_full = urllib.request.urlopen(config.get_url_log_full()).read()
    fggame_list = fgfparser.parse(html_full.decode(
        "utf-8"), base_url=config.get_url_log_full())
    print("last element in full " + str(len(fggame_list)) + ": " +
          fggame_list[-1].get_time() + ": " + fggame_list[-1].get_url())
