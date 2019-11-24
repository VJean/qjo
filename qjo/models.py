#!/usr/bin/env python3


class VenueParser:
    def get_events(self):
        raise NotImplementedError()


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
