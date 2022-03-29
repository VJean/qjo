import unittest

from urllib3 import PoolManager

from qjo.venues import Maroquinerie, Trianon


class TestVenues(unittest.TestCase):
    def setUp(self) -> None:
        self.pool = PoolManager()

    def test_maroquinerie(self):
        events = Maroquinerie.get_events(self.pool)
        self.assertGreater(len(events), 0)

    def test_trianon(self):
        events = Trianon.get_events(self.pool)
        self.assertGreater(len(events), 0)

    def tearDown(self) -> None:
        self.pool.clear()


if __name__ == "__main__":
    unittest.main()
