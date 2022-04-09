import unittest
from unittest.mock import Mock

from bs4 import BeautifulSoup

from qjo.models import Venue
from qjo.venues import Maroquinerie, Trianon, CabaretSauvage


def load_local_html(v: Venue) -> BeautifulSoup:
    venue_name = v.__name__.lower()
    path = f"tests/agendas/{venue_name}.html"
    with open(path) as f:
        content = f.read()
        return content


class TestVenues(unittest.TestCase):
    def setUp(self) -> None:
        Maroquinerie._get_agenda_html = Mock(
            return_value=BeautifulSoup(
                load_local_html(Maroquinerie), features="html.parser"
            )
        )
        Trianon._get_agenda_html = Mock(
            return_value=BeautifulSoup(load_local_html(Trianon), features="html.parser")
        )
        CabaretSauvage._get_agenda_html = Mock(
            return_value=BeautifulSoup(
                load_local_html(CabaretSauvage), features="html.parser"
            )
        )

    def test_maroquinerie(self):
        events = Maroquinerie.get_events()
        Maroquinerie._get_agenda_html.assert_called()
        self.assertEqual(len(events), 50)

    def test_trianon(self):
        events = Trianon.get_events()
        Trianon._get_agenda_html.assert_called()
        self.assertEqual(len(events), 115)

    def test_cabaret_sauvage(self):
        events = CabaretSauvage.get_events()
        CabaretSauvage._get_agenda_html.assert_called()
        self.assertEqual(len(events), 23)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
