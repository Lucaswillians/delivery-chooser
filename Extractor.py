import csv


class Extractor:
    CONNECTION_PATH = 'input/connections.csv'
    DELIVERIES_PATH = 'input/deliveries.csv'

    @staticmethod
    def get_connections():
        return Extractor.get_content(Extractor.CONNECTION_PATH)

    @staticmethod
    def get_deliveries():
        return Extractor.get_content(Extractor.DELIVERIES_PATH)

    @staticmethod
    def get_content(path):
        content = []
        first_line = False

        with open(path) as stream:
            rows = csv.reader(stream)

            for row in rows:
                if first_line is False:
                    first_line = True

                    continue

                content.append(row)

        return content
