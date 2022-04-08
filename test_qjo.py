import unittest


from qjo.venues import Maroquinerie, Trianon


class TestVenues(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_maroquinerie(self):
        events = Maroquinerie.get_events()
        self.assertGreater(len(events), 0)

    def test_trianon(self):
        events = Trianon.get_events()
        self.assertGreater(len(events), 0)

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()
