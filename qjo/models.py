#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib3, bs4


class Venue:
    url = NotImplemented
    address = NotImplemented

    @classmethod
    def get_name(cls):
        return cls.name if hasattr(cls, "name") else cls.__name__

    @classmethod
    def get_events(cls):
        raise NotImplementedError()

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        http = urllib3.PoolManager()
        r = http.request("GET", url)
        return bs4.BeautifulSoup(r.data, features="html.parser")


class Concert:
    def __init__(self, artist, date, infos=None):
        """
        'date' should hold following types: date or datetime
        """
        self.artist = artist
        self.date = date
        self.infos = infos

    def __repr__(self):
        rep_str = f"{str(self.date)}: {self.artist}"
        if self.infos is not None:
            rep_str += f" ({self.infos})"
        return rep_str
