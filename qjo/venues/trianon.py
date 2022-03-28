#!/usr/bin/env python3

from .. import models
from datetime import datetime, timedelta
import dateparser


def parse_date(date: str) -> datetime:
    return dateparser.parse(
        date,
        languages=["fr"],
        settings={
            "TIMEZONE": "Europe/Paris",
            "RETURN_AS_TIMEZONE_AWARE": True,
            "PREFER_DATES_FROM": "future",
        },
    )


class Trianon(models.Venue):
    name = "Le Trianon"
    url = "https://www.letrianon.fr"
    address = "80 Bd de Rochechouart, 75018 Paris"

    @classmethod
    def get_events(cls):
        soup = cls.get_soup("https://www.letrianon.fr/uk/billetterie")

        concerts = []

        events = soup.select("div.infos")
        for event in events:
            title = event.find("p", class_="titre")
            date = event.find("p", class_="date")
            if title is None or date is None:
                # return an array of errors maybe ?
                continue
            title = title.string.strip()
            date = date.string.strip()
            # Date is either a single date or a range of dates
            if date.startswith("From"):
                # string is like: 'From dd/mm/yyyy to dd/mm/yyyy'
                tokens = date.split()
                current_date = parse_date(tokens[1])
                end_date = parse_date(tokens[3])
                # Iterate over range:
                while current_date <= end_date:
                    concerts.append(models.Concert(title, current_date))
                    current_date += timedelta(days=1)
            else:
                parsed_date = parse_date(date)
                concerts.append(models.Concert(title, parsed_date))

        return concerts
