import csv


class Extractor:
    CONNECTION_PATH = 'input/connections.csv'
    DELIVERIES_PATH = 'input/deliveries.csv'

    @staticmethod
    def get_connections():
        content = []
        first_line = False

        with open(Extractor.CONNECTION_PATH) as stream:
            rows = csv.reader(stream)

            for row in rows:
                if first_line is False:
                    first_line = True

                    continue

                content.append(row)

        return content

    @staticmethod
    def get_deliveries():
        content = []
        first_line = False

        with open(Extractor.DELIVERIES_PATH) as stream:
            rows = csv.reader(stream)

            for row in rows:
                if first_line is False:
                    first_line = True

                    continue

                content.append({
                    'start_time': int(row[0].strip()),
                    'target': row[1].strip(),
                    'bonus': int(row[2].strip()),
                })

        return content
