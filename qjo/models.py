#!/usr/bin/env python3


class VenueParser:
    @classmethod
    def get_name(cls):
        return cls.name if hasattr(cls, 'name') else cls.__name__

    @classmethod
    def get_events(cls):
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
