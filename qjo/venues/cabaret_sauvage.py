#!/usr/bin/env python3

from .. import models
from . import parse_date
import dateparser


class CabaretSauvage(models.Venue):
    name = "Cabaret Sauvage"
    url = "https://www.cabaretsauvage.com/"
    agenda_url = "https://www.cabaretsauvage.com/agenda"
    address = models.Address("Parc de la Villette, 75019 Paris", "Paris", "France")

    @classmethod
    def _soup_to_concerts(cls, soup, concerts=[]):
        # select divs with role listitem
        # avoid the archives section
        items = soup.select("div[data-w-tab='Tab 3'] div[role=listitem]")
        for item in items:
            # filter only on category concert. This Tab 3 should only have concerts
            # but better make sure
            categ = item.select("a.category-link")[0]
            if categ["href"] == "/work-category/concert":
                details = item.select("div.work-details")[0]
                date = details.select("div.post-date")[0].text
                title = details.select("a.work-title")[0].text
                parsed_date = parse_date(
                    date,
                    date_formats=["%d.%m.%y", "%d.%m.%Y"],
                )
                concerts.append(models.Concert(title, parsed_date, cls))

        return concerts
