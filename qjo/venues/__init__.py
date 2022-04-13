#!/usr/bin/env python3

from datetime import datetime
import dateparser

__all__ = []


def parse_date(date: str, **kwargs) -> datetime:
    return dateparser.parse(
        date,
        languages=["fr"],
        settings={
            "TIMEZONE": "Europe/Paris",
            "RETURN_AS_TIMEZONE_AWARE": True,
            "PREFER_DATES_FROM": "future",
        },
        **kwargs
    )


from .maro import Maroquinerie
from .trianon import Trianon
from .cabaret_sauvage import CabaretSauvage

venues = [Maroquinerie, Trianon, CabaretSauvage]
