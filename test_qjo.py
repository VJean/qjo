import unittest

from qjo.venues import Maroquinerie

class TestVenues(unittest.TestCase):

    def test_maroquinerie(self):
        events = Maroquinerie.get_events()
        self.assertGreater(len(events), 0)

if __name__ == '__main__':
    unittest.main()