import unittest

from Extractor import Extractor

from DeliveryOptimizer import DeliveryOptimizer
from DeliveryOptimizerAI import DeliveryOptimizerAI

class TestExtractor(unittest.TestCase):
    def testConnections(self):
        connections = Extractor.get_connections()

        print(connections)
        self.assertGreater(len(connections), 0, 'deveria extrair as conexões')

    def testDeliveries(self):
        deliveries = Extractor.get_deliveries()

        print(deliveries)
        self.assertGreater(len(deliveries), 0, 'deveria extrair as entregas')

class TestDeliveryOptimizer(unittest.TestCase):
    def testCalculateDeliveries(self):
        optimizer = DeliveryOptimizer()
        optimizer.calculate_deliveries()
        self.assertGreater(optimizer.bonus_total, 0, 'deveria retornar valor de bônus sem IA')

class TestDeliveryOptimizerAI(unittest.TestCase):
    def testCalculateDeliveries(self):
        optimizer = DeliveryOptimizerAI(
            Extractor.get_connections(),
            Extractor.get_deliveries()
        )
        best_solution = optimizer.a_star_search()

        self.assertGreater(best_solution[0], 0, 'deveria retornar um total maior que 0 com IA')

    def testCalculateDeliveriesPath(self):
        optimizer = DeliveryOptimizerAI(
            Extractor.get_connections(),
            Extractor.get_deliveries()
        )
        best_solution = optimizer.a_star_search()

        self.assertTrue(len(best_solution[1]) > 0, 'deveria retornar os caminhos a se percorrer com IA')

if __name__ == "__main__":
    unittest.main()
