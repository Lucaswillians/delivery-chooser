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

    def _find_shortest_path(self, start, target, visited=None, current_time=0):
        if visited is None:
            visited = []

        # Se chegou ao nó de destino, retorna o tempo atual
        if start == target:
            return current_time

        # Marca o nó atual como visitado
        visited.append(start)

        # Verifica os vizinhos e calcula os tempos de viagem
        possible_paths = []
        for neighbor, travel_time in self.connections[start].items():
            if neighbor not in visited:
                total_time = current_time + travel_time
                path_time = self._find_shortest_path(neighbor, target, visited.copy(), total_time)
                if path_time is not None:
                    possible_paths.append(path_time)

        # Retorna o menor tempo entre todos os caminhos possíveis
        if possible_paths:
            return min(possible_paths)
        else:
            return None

    def calculate_deliveries(self):
        logging.info("Iniciando o cálculo das entregas...")
        for delivery in self.deliveries:
            start_time = delivery['start_time']
            target = delivery['target']
            bonus = delivery['bonus']
            logging.info(f"Processando entrega para {target} com bônus de {bonus} e tempo de início {start_time}.")

            # Get shortest path from 'A' to the delivery target using manual logic
            travel_time = self._find_shortest_path('A', target)

            if travel_time is not None:
                # Calculate the total time including start time
                arrival_time = start_time + travel_time
                if arrival_time <= start_time + bonus:
                    logging.info(f"Entrega para {target} no tempo! Bônus ganho: {bonus}")
                    self.bonus_total += bonus
                else:
                    logging.info(f"Entrega para {target} atrasada. Nenhum bônus.")
            else:
                logging.info(f"Nenhum caminho válido para {target}")

        logging.info(f"Total profit: {self.bonus_total}")
