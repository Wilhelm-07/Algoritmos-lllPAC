class WeightedGraph:
    def __init__(self):
        self._adjMat = {}  # Matriz de adyacencia como un dict

    def addEdge(self, src, dest, weight):
        """Agrega una arista ponderada entre src y dest."""
        if src not in self._adjMat:
            self._adjMat[src] = {}
        self._adjMat[src][dest] = weight

    def allShortestPathsMatrix(self):
        """Calcula todas las rutas más cortas usando Floyd-Warshall."""
        # Crear una lista de nodos
        nodes = list(self._adjMat.keys())
        n = len(nodes)
        
        # Inicializar la matriz de distancias
        dist = {u: {v: float('inf') for v in nodes} for u in nodes}
        for u in nodes:
            dist[u][u] = 0  # La distancia a sí mismo es 0
            if u in self._adjMat:
                for v, weight in self._adjMat[u].items():
                    dist[u][v] = weight  # Usar pesos de las aristas

        # Aplicar el algoritmo de Floyd-Warshall
        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def printAdjMatrix(self):
        """Imprime la matriz de adyacencia."""
        for src, destinations in self._adjMat.items():
            for dest, weight in destinations.items():
                print(f"{src} -> {dest}: {weight}")

# Demostración con los tiempos de tren de la Figura 15-13
graph = WeightedGraph()
edges = [
    ('A', 'B', 3), ('A', 'C', 8), ('A', 'D', float('inf')), 
    ('B', 'C', float('inf')), ('B', 'D', 1), 
    ('C', 'A', 4), ('C', 'D', float('inf')), 
    ('D', 'A', 2), ('D', 'C', 5)
]

for src, dest, weight in edges:
    graph.addEdge(src, dest, weight)

print("Matriz de adyacencia:")
graph.printAdjMatrix()

print("\nMatriz de distancias mínimas:")
distances = graph.allShortestPathsMatrix()
for src, dests in distances.items():
    for dest, cost in dests.items():
        print(f"{src} -> {dest}: {cost}")
