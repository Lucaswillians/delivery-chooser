import unittest

from Extractor import Extractor
from DeliveryOptimizer import DeliveryOptimizer
from DeliveryOptimizerAI import DeliveryOptimizerAI

class TestExtractor(unittest.TestCase):
    def testConnections(self):
        connections = Extractor.get_connections()

        self.assertGreater(len(connections), 0, 'deveria extrair as conexões do arquivo')

    def testDeliveries(self):
        deliveries = Extractor.get_deliveries()

        self.assertGreater(len(deliveries), 0, 'deveria extrair as entregas do arquivo')

class TestDeliveryOptimizer(unittest.TestCase):
    def testCalculateDeliveries(self):
        optimizer = DeliveryOptimizer()
        optimizer.calculate_deliveries()

        self.assertGreater(optimizer.bonus_total, 0, 'bônus sem IA deveria ser maior que 0')

class TestDeliveryOptimizerAI(unittest.TestCase):
    def testCalculateDeliveriesBonus(self):
        optimizer = DeliveryOptimizerAI(
            Extractor.get_connections(),
            Extractor.get_deliveries()
        )
        best_solution = optimizer.a_star_search()

        self.assertGreater(best_solution[0], 0, 'bônus com IA deveria ser maior que 0')

    def testCalculateDeliveriesPath(self):
        optimizer = DeliveryOptimizerAI(
            Extractor.get_connections(),
            Extractor.get_deliveries()
        )
        best_solution = optimizer.a_star_search()

        self.assertTrue(len(best_solution[1]) > 0, 'caminho retornado com IA não deve ser vazio')

if __name__ == "__main__":
    unittest.main()
