import heapq
from Extractor import Extractor

class DeliveryOptimizer:
    def __init__(self):
        self.connections = self._parse_connections(Extractor.get_connections())
        self.deliveries = Extractor.get_deliveries()
        self.bonus_total = 0

    def _parse_connections(self, connection_data):
        graph = {}
        nodes = ['A', 'B', 'C', 'D']
        for i, row in enumerate(connection_data):
            graph[nodes[i]] = {}
            for j, time in enumerate(row):
                if int(time) > 0:
                    graph[nodes[i]][nodes[j]] = int(time)
        return graph

    def _dijkstra(self, start):
        # Dijkstra algorithm to find the shortest path from start to all other nodes
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
        return distances

    def calculate_deliveries(self):
        for delivery in self.deliveries:
            start_time = delivery['start_time']
            target = delivery['target']
            bonus = delivery['bonus']

            # Get shortest path from 'A' to the delivery target
            shortest_paths = self._dijkstra('A')
            travel_time = shortest_paths.get(target, float('infinity'))

            if travel_time != float('infinity'):
                # Calculate the total time including start time
                arrival_time = start_time + travel_time
                if arrival_time <= start_time + bonus:
                    print(f"Delivery to {target} on time! Bonus earned: {bonus}")
                    self.bonus_total += bonus
                else:
                    print(f"Delivery to {target} late. No bonus earned.")
            else:
                print(f"No valid path to {target}")

        print(f"Total bonus earned: {self.bonus_total}")

if __name__ == "__main__":
    optimizer = DeliveryOptimizer()
    optimizer.calculate_deliveries()
