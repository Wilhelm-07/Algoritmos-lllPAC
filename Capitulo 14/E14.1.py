class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {chr(i): [] for i in range(65, 75)}  # A to J

    def add_edge(self, u, v):
        """Añadir una arista entre u y v. Para grafos dirigidos, sólo se añade en una dirección"""
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def print_graph(self):
        """Imprime el grafo. Para grafos dirigidos, imprime aristas como u -> v"""
        for node, neighbors in self.adj_list.items():
            neighbors_str = ' -> '.join(neighbors)
            print(f"{node} -> {neighbors_str}")

    def depthFirst(self, start):
        """Realiza un recorrido en profundidad (DFS) desde el vértice start"""
        visited = set()
        self._depthFirstUtil(start, visited)
        print()

    def _depthFirstUtil(self, node, visited):
        """Utiliza DFS recursivo para visitar todos los vértices desde el nodo actual"""
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._depthFirstUtil(neighbor, visited)

# Crear un grafo dirigido
directed_graph = Graph(directed=True)
edges_directed = [('AG', 'AI'), ('CF', 'DA'), ('DI', 'HD'), ('HE', 'HF'),
                  ('HG', 'IH'), ('JC', 'JH')]
for u, v in edges_directed:
    directed_graph.add_edge(u, v)

print("Grafo dirigido:")
directed_graph.print_graph()
print("DFS desde J en grafo dirigido:")
directed_graph.depthFirst('J')

# Crear un grafo no dirigido
undirected_graph = Graph()
edges_undirected = [('AG', 'AI'), ('CF', 'DA'), ('DI', 'HD'), ('HE', 'HF'),
                    ('HG', 'IH'), ('JC', 'JH')]
for u, v in edges_undirected:
    undirected_graph.add_edge(u, v)

print("\nGrafo no dirigido:")
undirected_graph.print_graph()
print("DFS desde J en grafo no dirigido:")
undirected_graph.depthFirst('J')
