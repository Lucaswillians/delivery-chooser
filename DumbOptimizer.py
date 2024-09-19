import csv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("delivery_optimizer.log"),
        logging.StreamHandler()
    ]
)

class Extractor:
    CONNECTION_PATH = 'input/connections.csv'
    DELIVERIES_PATH = 'input/deliveries.csv'

    @staticmethod
    def get_connections():
        content = []
        with open(Extractor.CONNECTION_PATH) as stream:
            rows = csv.reader(stream)
            for row in rows:
                content.append([cell.strip() for cell in row])
        return content

    @staticmethod
    def get_deliveries():
        content = []
        with open(Extractor.DELIVERIES_PATH) as stream:
            rows = csv.reader(stream)
            next(rows)
            for row in rows:
                content.append({
                    'start_time': int(row[0].strip()),
                    'target': row[1].strip(),
                    'bonus': int(row[2].strip()),
                })
        return content

class SimpleDeliveryOptimizer:
    def __init__(self, connections, deliveries):
        logging.info("Iniciando SimpleDeliveryOptimizer...")
        self.connections = self._parse_connections(connections)
        self.deliveries = deliveries
        self.bonus_total = 0
        logging.info("Dados carregados. Conexões e entregas foram processadas.")

    def _parse_connections(self, connection_data):
        logging.info("Processando conexões...")
        graph = {}
        nodes = connection_data[0]

        for i, row in enumerate(connection_data[1:]):
            graph[nodes[i]] = {}
            for j, time in enumerate(row):
                if int(time) > 0:
                    graph[nodes[i]][nodes[j]] = int(time)
        logging.info("Conexões processadas com sucesso.")
        return graph

    def calculate_deliveries(self):
        logging.info("Iniciando o cálculo das entregas...")
        for delivery in self.deliveries:
            start_time = delivery['start_time']
            target = delivery['target']
            bonus = delivery['bonus']
            logging.info(f"Processando entrega para {target} com bônus de {bonus} e tempo de início {start_time}.")

            if target in self.connections['A']:
                travel_time = self.connections['A'][target]
                arrival_time = start_time + travel_time

                if arrival_time <= start_time + bonus:
                    logging.info(f"Entrega para {target} no tempo! Bônus ganho: {bonus}")
                    self.bonus_total += bonus
                else:
                    logging.info(f"Entrega para {target} atrasada. Nenhum bônus.")
            else:
                logging.info(f"Nenhum caminho válido para {target}")

        logging.info(f"Bônus total ganho: {self.bonus_total}")

def main():
    connections = Extractor.get_connections()
    deliveries = Extractor.get_deliveries()

    optimizer = SimpleDeliveryOptimizer(connections, deliveries)
    optimizer.calculate_deliveries()

if __name__ == '__main__':
    main()
