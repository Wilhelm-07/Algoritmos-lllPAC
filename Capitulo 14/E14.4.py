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

    def connectivityMatrix(self):
        """Devuelve la matriz de conectividad utilizando el algoritmo de Warshall"""
        # Inicializamos la matriz de conectividad con la copia de la matriz de adyacencia
        n = len(self.adj_list)
        matrix = {k: {j: False for j in self.adj_list} for k in self.adj_list}
        for i, row in self.adj_list.items():
            for j in row:
                matrix[i][j] = True
        
        # Aplicar el algoritmo de Warshall
        for k in self.adj_list:
            for i in self.adj_list:
                for j in self.adj_list:
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        
        return matrix

    def hasCycles(self):
        """Devuelve True si el grafo tiene ciclos, False en caso contrario"""
        connectivity_matrix = self.connectivityMatrix()
        
        # Buscar ciclos en la matriz de conectividad
        for i in self.adj_list:
            if connectivity_matrix[i][i]:
                return True
        
        return False

# Crear el grafo dirigido de la Figura 14-22
directed_graph = Graph(directed=True)
edges_directed = [('AG', 'AI'), ('CF', 'DA'), ('DI', 'HD'), ('HE', 'HF'),
                  ('HG', 'IH'), ('JC', 'JH')]
for u, v in edges_directed:
    directed_graph.add_edge(u, v)

# Mostrar la matriz de conectividad y verificar si tiene ciclos
print("Matriz de conectividad para el grafo dirigido:")
connectivity_matrix = directed_graph.connectivityMatrix()
for row in connectivity_matrix.values():
    print(row)

print("\n¿Hay ciclos en el grafo dirigido?")
print(directed_graph.hasCycles())

# Crear el grafo no dirigido de la Figura 14-23
undirected_graph = Graph()
edges_undirected = [('AG', 'AI'), ('CF', 'DA'), ('DI', 'HD'), ('HE', 'HF'),
                    ('HG', 'IH'), ('JC', 'JH')]
for u, v in edges_undirected:
    undirected_graph.add_edge(u, v)

# Mostrar la matriz de conectividad y verificar si tiene ciclos
print("\nMatriz de conectividad para el grafo no dirigido:")
connectivity_matrix = undirected_graph.connectivityMatrix()
for row in connectivity_matrix.values():
    print(row)

print("\n¿Hay ciclos en el grafo no dirigido?")
print(undirected_graph.hasCycles())
