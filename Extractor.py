import csv

class Extractor:
    CONNECTION_PATH = 'input/connections.csv'
    DELIVERIES_PATH = 'input/deliveries.csv'

    @staticmethod
    def get_connections():
        connections = []
        first_line = False

        with open(Extractor.CONNECTION_PATH) as stream:
            rows = csv.reader(stream)

            for row in rows:
                if first_line is False:
                    first_line = True

                    continue

                connections.append(row)

        return connections

    @staticmethod
    def get_deliveries():
        deliveries = []
        first_line = False

        with open(Extractor.DELIVERIES_PATH) as stream:
            rows = csv.reader(stream)

            for row in rows:
                if first_line is False:
                    first_line = True

                    continue

                deliveries.append(row)

        return deliveries
