import unittest

from Extractor import Extractor


class TestExtractor(unittest.TestCase):
    def testConnections(self):
        self.assertGreater(len(Extractor.get_connections()), 0)

    def testDeliveries(self):
        self.assertGreater(len(Extractor.get_deliveries()), 0)


if __name__ == '__main__':
    unittest.main()
