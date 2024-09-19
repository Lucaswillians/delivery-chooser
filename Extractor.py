import csv

from DeliveryOptimizerAI import DeliveryOptimizerAI

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
            next(rows)  # Skip header
            for row in rows:
                content.append([cell.strip() for cell in row])  # Remove extra spaces
        return content

    @staticmethod
    def get_deliveries():
        content = []
        with open(Extractor.DELIVERIES_PATH) as stream:
            rows = csv.reader(stream)
            next(rows)  # Skip header
            for row in rows:
                content.append({
                    'start_time': int(row[0].strip()),
                    'target': row[1].strip(),
                    'bonus': int(row[2].strip()),
                })
        return content

def main():
    connections = Extractor.get_connections()
    deliveries = Extractor.get_deliveries()

    optimizer = DeliveryOptimizerAI(connections, deliveries)
    best_solution = optimizer.a_star_search()

if __name__ == '__main__':
    main()
