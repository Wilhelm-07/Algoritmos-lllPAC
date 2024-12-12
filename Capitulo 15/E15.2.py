class WeightedDiGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight

    def all_max_paths(self):
        def dfs(node, path):
            yield path
            for neighbor, weight in self.graph.get(node, {}).items():
                if neighbor not in path:
                    yield from dfs(neighbor, path + [(neighbor, weight)])

        for node in self.graph:
            yield from dfs(node, [(node, None)])

    def hamiltonian_paths(self):
        for path in self.all_max_paths():
            if len(path) == len(self.graph):
                yield path