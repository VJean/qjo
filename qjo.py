#!/usr/bin/env python3

import urllib3, bs4, locale
import datetime as dt
import dateparser

from qjo.venues import Maroquinerie


for c in Maroquinerie.get_events():
    print(c)
