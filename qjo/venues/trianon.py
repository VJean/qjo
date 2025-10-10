#!/usr/bin/env python3

from .. import models
from . import parse_date
from datetime import datetime, timedelta
import re


class Trianon(models.Venue):
    name = "Le Trianon"
    url = "https://www.letrianon.fr"
    agenda_url = "https://www.letrianon.fr/fr/programmation/"
    address = models.Address("80 Bd de Rochechouart, 75018 Paris", "Paris", "France")

    date_range_re = re.compile("du \w+ (?P<from>\d+ \w+) au (?P<to>\d+ \w+) (?P<year>\d+)")

    @classmethod
    def _soup_to_concerts(cls, soup, concerts=[]):
        events = soup.select("div.t")
        for event in events:
            title = event.find("div", class_="titre")
            date = event.find("div", class_="date")
            if title is None or date is None:
                # return an array of errors maybe ?
                continue
            title = title.string.strip()
            date = " ".join(item.string.strip() for item in date.contents)
            # Date is either a single date or a range of dates
            match_range = cls.date_range_re.match(date)
            if match_range:
                # string is like: 'du dimanche 11 février au 13 février 2024'
                current_date = parse_date(match_range.group('from') + ' ' + match_range.group('year'))
                end_date = parse_date(match_range.group('to') + ' ' + match_range.group('year'))
                # Iterate over range:
                while current_date <= end_date:
                    concerts.append(models.Concert(title, current_date, cls))
                    current_date += timedelta(days=1)
            else:
                parsed_date = parse_date(date)
                concerts.append(models.Concert(title, parsed_date, cls))

        return concerts
