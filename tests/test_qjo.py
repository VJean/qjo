import logging
import unittest
from unittest.mock import Mock
from datetime import date, datetime

from bs4 import BeautifulSoup

from qjo.models import Concert, Venue
from qjo.venues import Maroquinerie, Trianon, CabaretSauvage, parse_date
from qjo import filter_events

logging.basicConfig(format='[%(asctime)s][%(name)s][%(process)d][%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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


class TestConcert(unittest.TestCase):
    def test_comparison(self):
        c1 = Concert("A", parse_date("11/04/2022"), Maroquinerie, infos="Canceled")
        c2 = Concert(
            "A", parse_date("11/04/2022 19:30"), Maroquinerie, infos="Canceled"
        )
        self.assertNotEqual(c1, c2)
        self.assertLess(c1, c2)
        self.assertLessEqual(c1, c2)
        self.assertGreater(c2, c1)
        self.assertGreaterEqual(c2, c1)

        c3 = Concert("A", parse_date("11/04/2022"), Maroquinerie, infos="Canceled")
        self.assertEqual(c1, c3)
        self.assertLessEqual(c1, c3)
        self.assertGreaterEqual(c2, c3)

        c3.artist = "B"
        self.assertNotEqual(c1, c3)

    def test_sort(self):
        c1 = Concert("A", parse_date("11/04/2022"), Maroquinerie, infos="Canceled")
        c2 = Concert("B", parse_date("11/04/2022"), Maroquinerie)
        c3 = Concert("A", parse_date("11/04/2022 19:30"), Trianon)
        c4 = Concert("B", parse_date("25/06/2022 20:00"), CabaretSauvage)
        events = [c1, c4, c3, c2]
        events.sort()
        self.assertListEqual(events, [c1, c2, c3, c4])


class TestFilter(unittest.TestCase):
    def test_filter(self):
        c1 = Concert("Artist One", parse_date("11/04/2022"), Maroquinerie)
        c2 = Concert("Second Artist", parse_date("11/04/2022"), Maroquinerie)
        c3 = Concert("SUPERBAND", parse_date("11/04/2022 19:30"), Trianon)
        c4 = Concert("local band", parse_date("25/06/2022 20:00"), CabaretSauvage)
        c5 = Concert(
            "Artist One + local band",
            date(2022, 6, 26),
            Trianon,
            infos="Artist One with local band as opener",
        )
        events = [c1, c2, c3, c4, c5]
        self.assertListEqual(
            filter_events(events, ["local band", "Second Artist", "obscure band"]),
            [c2, c4, c5],
        )


if __name__ == "__main__":
    unittest.main()
