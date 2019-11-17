#!/usr/bin/env python3

import urllib3, bs4, locale
import datetime as dt

# use another lib for handling timezones ?


class Concert:
    def __init__(self, artist, date, venue, infos=None):
        """
        'date' should hold following types: date or datetime
        """
        self.artist = artist
        self.date = date
        self.venue = venue
        self.infos = infos

    def __repr__(self):
        rep_str = f"{str(self.date)}: {self.artist}, {self.venue}"
        if self.infos is not None:
            rep_str += f" ({self.infos})"
        return rep_str


http = urllib3.PoolManager()
r = http.request("GET", "http://www.lamaroquinerie.fr/fr/agenda/")
soup = bs4.BeautifulSoup(r.data, features="html.parser")
events = soup.select("li.event")

# set locale FR en fonction de Windows ou Linux (pas la même syntaxe)
locale.setlocale(locale.LC_ALL, "fr_FR.utf8")
today_day = dt.datetime.today().day
today_month = dt.datetime.today().month
today_year = dt.datetime.today().year

concerts = []

for event in events:
    title = event.find("h2")
    date = event.find("h3", class_="date")
    time = event.find("div", class_="time")
    details = event.find("div", class_="description")
    title = "" if title is None or title.string is None else title.string.strip()
    date = "" if date is None or date.string is None else date.string.strip()
    time = "" if time is None or time.string is None else time.string.strip()
    details = (
        None if details is None or details.string is None else details.string.strip()
    )

    dates = []

    if date != "":
        # dates are expected to be written as "14 Janvier" or range "14 Janvier - 17 Janvier"
        for d in map(lambda x: x.strip(), date.split("-")):
            try:
                event_date = dt.datetime.strptime(d, "%d %B")
            except ValueError:
                print("Could not parse date: ", d)
                continue
            # which year ? all events are in the future
            if event_date.month > today_month:
                year = today_year
            elif event_date.month < today_month:
                year = today_year + 1
            else:
                if event_date.day >= today_day:
                    year = today_year
                else:
                    year = today_year + 1

            event_date = event_date.replace(year=year)

            if time != "":
                t = dt.datetime.strptime(time, "%H:%M")
                event_date = event_date.replace(hour=t.hour, minute=t.minute)
                event_date_str = event_date.strftime("%d/%m/%Y %H:%M")
            else:
                event_date_str = event_date.strftime("%d/%m/%Y")
                event_date = event_date.date()

            dates.append(event_date)

        if len(dates) == 1:
            concerts.append(Concert(title, dates[0], "La Maroquinerie", details))
        elif len(dates) == 2:
            # unpack
            first, last = dates
            # generate dates range
            concerts.append(Concert(title, first, "La Maroquinerie", details))
            while first != last:
                first = first + dt.timedelta(days=1)
                concerts.append(Concert(title, first, "La Maroquinerie", details))
        else:
            print("Got a strange date format : ", date)
            continue

for c in concerts:
    print(c)
