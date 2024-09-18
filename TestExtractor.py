import unittest

from Extractor import Extractor


class TestExtractor(unittest.TestCase):
    def testConnections(self):
        connections = Extractor.get_connections()

        print(connections)
        self.assertGreater(len(connections), 0)

    def testDeliveries(self):
        deliveries = Extractor.get_deliveries()

        print(deliveries)
        self.assertGreater(len(deliveries), 0)


if __name__ == '__main__':
    unittest.main()
