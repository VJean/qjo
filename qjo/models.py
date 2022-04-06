#!/usr/bin/env python3

from typing import Sequence, List
from bs4 import BeautifulSoup
import urllib3, bs4
from urllib3 import PoolManager


class Address:
    def __init__(self, full, city, country):
        self.full = full
        self.city = city
        self.country = country

    def __repr__(self):
        return f"{self.full} ({self.city}, {self.country})"


class Concert:
    def __init__(self, artist, date, venue, infos=None):
        """
        'date' should hold following types: date or datetime
        """
        self.artist = artist
        self.date = date
        self.infos = infos
        self.venue = venue

    def __repr__(self):
        rep_str = f"{str(self.date)}: {self.artist} at {self.venue.get_name()}"
        if self.infos is not None:
            rep_str += f" ({self.infos})"
        return rep_str


class Venue:
    url = NotImplemented
    agenda_url = NotImplemented
    address = NotImplemented
    http_pool = PoolManager()

    @classmethod
    def get_name(cls):
        return cls.name if hasattr(cls, "name") else cls.__name__

    @classmethod
    def get_events(cls):
        soup = cls._get_agenda_html()
        return cls._soup_to_concerts(soup)

    @classmethod
    def _soup_to_concerts(
        cls, soup: BeautifulSoup, concerts: Sequence[Concert]
    ) -> List[Concert]:
        raise NotImplementedError()

    @classmethod
    def _get_agenda_html(cls) -> BeautifulSoup:
        return cls._get_soup(cls.agenda_url)

    @classmethod
    def _get_soup(cls, url: str) -> BeautifulSoup:
        r = cls.http_pool.request("GET", url)
        return bs4.BeautifulSoup(r.data, features="html.parser")
