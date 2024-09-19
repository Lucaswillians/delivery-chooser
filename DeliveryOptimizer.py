import heapq
import logging
from Extractor import Extractor

# Configure o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryOptimizer:
    def __init__(self):
        logging.info("Iniciando DeliveryOptimizer...")
        self.connections = self._parse_connections(Extractor.get_connections())
        self.deliveries = Extractor.get_deliveries()
        self.bonus_total = 0
        logging.info("Dados carregados. Conexões e entregas foram processadas.")

    def _parse_connections(self, connection_data):
        logging.info("Processando conexões...")
        graph = {}
        nodes = ['A', 'B', 'C', 'D']

        connection_data = connection_data[1:]

        for i, row in enumerate(connection_data):
            graph[nodes[i]] = {}

            for j, time in enumerate(row):
                if int(time) > 0:
                    graph[nodes[i]][nodes[j]] = int(time)
        logging.info("Conexões processadas com sucesso.")
        return graph

    def _dijkstra(self, start):
        logging.info(f"Calculando o caminho mais curto a partir de {start}...")
        distances = {node: float('infinity') for node in self.connections}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.connections[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        logging.info(f"Caminho mais curto calculado: {distances}")
        return distances

    def calculate_deliveries(self):
        logging.info("Iniciando o cálculo das entregas...")
        for delivery in self.deliveries:
            start_time = delivery['start_time']
            target = delivery['target']
            bonus = delivery['bonus']
            logging.info(f"Processando entrega para {target} com bônus de {bonus} e tempo de início {start_time}.")

            # Get shortest path from 'A' to the delivery target
            shortest_paths = self._dijkstra('A')
            travel_time = shortest_paths.get(target, float('infinity'))

            if travel_time != float('infinity'):
                # Calculate the total time including start time
                arrival_time = start_time + travel_time
                if arrival_time <= start_time + bonus:
                    logging.info(f"Entrega para {target} no tempo! Bônus ganho: {bonus}")
                    self.bonus_total += bonus
                else:
                    logging.info(f"Entrega para {target} atrasada. Nenhum bônus.")
            else:
                logging.info(f"Nenhum caminho válido para {target}")

        logging.info(f"Bônus total ganho: {self.bonus_total}")
