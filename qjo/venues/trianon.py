#!/usr/bin/env python3

from .. import models
import urllib3, bs4
import datetime as dt
import dateparser

class Trianon(models.Venue):
    name = "Le Trianon"
    url = "80 Bd de Rochechouart, 75018 Paris"
    address = "https://www.letrianon.fr"

    @classmethod
    def get_events(cls):
        http = urllib3.PoolManager()
        r = http.request("GET", "https://www.letrianon.fr/uk/billetterie")
        soup = bs4.BeautifulSoup(r.data, features="html.parser")
        
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

        
        return concerts
