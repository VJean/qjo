#!/usr/bin/env python3

from .maro import Maroquinerie
from .trianon import Trianon
from .cabaret_sauvage import CabaretSauvage

__all__ = []

venues = [Maroquinerie, Trianon, CabaretSauvage]
