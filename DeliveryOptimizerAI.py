import logging
import heapq

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("delivery_optimizer.log"),
        logging.StreamHandler()
    ]
)

class DeliveryOptimizerAI:
    def __init__(self, connections, deliveries):
        self.graph = self.build_graph(connections)
        self.deliveries = sorted(deliveries, key=lambda x: x['start_time'])
        self.start_point = 'A'

    def build_graph(self, connections):
        graph = {}
        nodes = connections[0]  # First row contains nodes

        logging.info("Building graph with nodes: %s", nodes)

        for i in range(1, len(connections)):
            for j in range(len(connections[i])):
                if int(connections[i][j]) != 0:  # If there's a connection
                    src = nodes[i - 1]  # Row corresponds to source node
                    dest = nodes[j]  # Column corresponds to destination node
                    time = int(connections[i][j])  # Travel time between them

                    logging.info("Adding edge from %s to %s with time %d", src, dest, time)

                    if src not in graph:
                        graph[src] = []
                    graph[src].append((dest, time))

                    if dest not in graph:
                        graph[dest] = []
                    graph[dest].append((src, time))

        logging.info("Graph built: %s", graph)
        return graph

    def a_star_search(self):
        pq = []
        heapq.heappush(pq, (0, 0, self.start_point, []))  # (current time, total bonus, current location, delivery path)
        best_solution = (0, [])  # (total bonus, delivery path)

        logging.info("Initial deliveries: %s", self.deliveries)

        while pq:
            current_time, current_bonus, current_location, path = heapq.heappop(pq)
            logging.info("Exploring: current_time=%d, current_bonus=%d, current_location=%s, path=%s",
                         current_time, current_bonus, current_location, path)

            if current_bonus > best_solution[0]:
                best_solution = (current_bonus, path)

            for delivery in self.deliveries:
                if delivery['target'] not in path:
                    time_to_target = self.get_time_between(current_location, delivery['target'])
                    if time_to_target is not None:
                        new_time = max(current_time + time_to_target, delivery['start_time'])
                        logging.info("Considering delivery to %s: new_time=%d, delivery_start_time=%d",
                                     delivery['target'], new_time, delivery['start_time'])

                        new_path = path + [delivery['target']]
                        new_bonus = current_bonus + delivery['bonus']

                        return_time = self.get_time_between(delivery['target'], self.start_point)
                        if return_time is not None:
                            new_time += return_time
                            heapq.heappush(pq, (new_time, new_bonus, self.start_point, new_path))
                            logging.info("Pushing to queue: new_time=%d, new_bonus=%d, path=%s",
                                         new_time, new_bonus, new_path)

        logging.info("Best solution found: %s", best_solution)
        return best_solution

    def get_time_between(self, src, dest):
        for neighbor, time in self.graph.get(src, []):
            if neighbor == dest:
                return time
        return None
