#!/usr/bin/env python3


class Venue:
    @classmethod
    def get_name(cls):
        return cls.name if hasattr(cls, 'name') else cls.__name__

    @classmethod
    def get_events(cls):
        raise NotImplementedError()


class Concert:
    def __init__(self, artist, date, infos=None):
        """
        'date' should hold following types: date or datetime
        """
        self.artist = artist
        self.date = date
        self.infos = infos

    def __repr__(self):
        rep_str = f"{str(self.date)}: {self.artist}"
        if self.infos is not None:
            rep_str += f" ({self.infos})"
        return rep_str
