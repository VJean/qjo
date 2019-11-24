#!/usr/bin/env python3

import urllib3, bs4, locale
import datetime as dt
import dateparser

from qjo.venues import venues

print("Available venues: ", venues.keys())

if 'Maroquinerie' in venues.keys():
    print(venues['Maroquinerie'].get_events())

