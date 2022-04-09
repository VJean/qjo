#!/usr/bin/env python3

from .. import models
import datetime as dt
import dateparser


class CabaretSauvage(models.Venue):
    name = "Cabaret Sauvage"
    url = "https://www.cabaretsauvage.com/"
    agenda_url = "https://www.cabaretsauvage.com/agenda"
    address = models.Address("Parc de la Villette, 75019 Paris", "Paris", "France")

    @classmethod
    def _soup_to_concerts(cls, soup, concerts=[]):
        return concerts
