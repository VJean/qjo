#!/usr/bin/env python3

import logging
from .. import models
from . import parse_date
import datetime as dt

logger = logging.getLogger(__name__)

class Maroquinerie(models.Venue):
    name = "La Maroquinerie"
    url = "http://www.lamaroquinerie.fr"
    agenda_url = "http://www.lamaroquinerie.fr/fr/agenda"
    address = models.Address("Rue Boyer, 75020 Paris", "Paris", "France")

    @classmethod
    def _soup_to_concerts(cls, soup, concerts=[]):
        events = soup.select("li.event")

        today_day = dt.datetime.today().day
        today_month = dt.datetime.today().month
        today_year = dt.datetime.today().year

        for event in events:
            title = event.find("h2")
            date = event.find("h3", class_="date")
            time = event.find("div", class_="time")
            details = event.find("div", class_="description")
            title = (
                "" if title is None or title.string is None else title.string.strip()
            )
            date = "" if date is None or date.string is None else date.string.strip()
            time = "" if time is None or time.string is None else time.string.strip()
            details = (
                None
                if details is None or details.string is None
                else details.string.strip()
            )

            dates = []

            if date != "":
                # dates are expected to be written as "14 Janvier" or range "14 Janvier - 17 Janvier"
                for d in map(lambda x: x.strip(), date.split("-")):
                    event_date = parse_date(
                        f"{d} {time}",
                    )
                    if event_date is None:
                        logger.warning(f"Could not parse date '{d}' for title '{title}'")
                        continue
                    # which year ? all events are either today or in the future
                    if event_date.day == today_day and event_date.month == today_month:
                        event_date = event_date.replace(year=today_year)

                    dates.append(event_date)

                if len(dates) == 1:
                    concerts.append(models.Concert(title, dates[0], cls, details))
                elif len(dates) == 2:
                    # unpack
                    first, last = dates
                    # generate dates range
                    concerts.append(models.Concert(title, first, cls, details))
                    while first != last:
                        first = first + dt.timedelta(days=1)
                        concerts.append(models.Concert(title, first, cls, details))
                else:
                    logger.warning(f"Unknown date format '{d}' for title '{title}'")
                    continue
        return concerts
