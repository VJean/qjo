#!/usr/bin/env python3

from .maro import Maroquinerie
from .trianon import Trianon

__all__=[]

venues = { Maroquinerie.get_name() : Maroquinerie,
Trianon.get_name(): Trianon }
