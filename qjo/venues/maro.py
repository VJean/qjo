#!/usr/bin/env python3

from .. import models
import datetime as dt
import dateparser


class Maroquinerie(models.Venue):
    name = "La Maroquinerie"
    url = "http://www.lamaroquinerie.fr"
    address = "Rue Boyer, 75020 Paris"

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
                    event_date = dateparser.parse(
                        f"{d} {time}",
                        languages=["fr"],
                        settings={
                            "TIMEZONE": "Europe/Paris",
                            "RETURN_AS_TIMEZONE_AWARE": True,
                            "PREFER_DATES_FROM": "future",
                        },
                    )
                    if event_date is None:
                        print("Could not parse date: ", d)
                        continue
                    # which year ? all events are either today or in the future
                    if event_date.day == today_day and event_date.month == today_month:
                        event_date = event_date.replace(year=today_year)

                    if time == "":
                        event_date = event_date.date()

                    dates.append(event_date)

                if len(dates) == 1:
                    concerts.append(models.Concert(title, dates[0], details))
                elif len(dates) == 2:
                    # unpack
                    first, last = dates
                    # generate dates range
                    concerts.append(models.Concert(title, first, details))
                    while first != last:
                        first = first + dt.timedelta(days=1)
                        concerts.append(models.Concert(title, first, details))
                else:
                    print("Got a strange date format : ", date)
                    continue
        return concerts

    @classmethod
    def get_events(cls):
        soup = cls._get_soup("http://www.lamaroquinerie.fr/fr/agenda/")

        return cls._soup_to_concerts(soup)
