import itertools

class DirectedGraph:
    def __init__(self):
        self._adjMat = {}

    def addEdge(self, src, dest, weight):
        """Agrega una arista ponderada entre src y dest."""
        if src not in self._adjMat:
            self._adjMat[src] = {}
        self._adjMat[src][dest] = weight

    def getEdgeWeight(self, src, dest):
        """Obtiene el peso de la arista entre src y dest, o infinito si no existe."""
        return self._adjMat.get(src, {}).get(dest, float('inf'))

    def tsp(self):
        """Resuelve el problema del vendedor ambulante usando fuerza bruta."""
        cities = list(self._adjMat.keys())
        n = len(cities)

        if n == 0:
            return [], 0  # No hay ciudades
        if n == 1:
            return cities, 0  # Una sola ciudad

        shortest_path = None
        min_cost = float('inf')

        for perm in itertools.permutations(cities):
            # Calcular el costo del recorrido para la permutación actual
            current_cost = 0
            for i in range(n - 1):
                current_cost += self.getEdgeWeight(perm[i], perm[i + 1])

            # Agregar el costo de regreso a la ciudad inicial
            current_cost += self.getEdgeWeight(perm[-1], perm[0])

            # Actualizar la mejor solución encontrada
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_path = perm

        return list(shortest_path), min_cost


# Demostración con la Figura 15-21 y variaciones en los tiempos de retorno
def demo_tsp():
    variations = [
        ("Tiempo de retorno igual", 0),
        ("Tiempo de retorno +5 minutos", 5),
        ("Tiempo de retorno +10 minutos", 10),
    ]

    # Grafo inicial
    graph = DirectedGraph()
    edges = [
        ('A', 'B', 10), ('A', 'C', 15), ('A', 'D', 20),
        ('B', 'A', 10), ('B', 'C', 35), ('B', 'D', 25),
        ('C', 'A', 15), ('C', 'B', 35), ('C', 'D', 30),
        ('D', 'A', 20), ('D', 'B', 25), ('D', 'C', 30),
    ]

    for src, dest, weight in edges:
        graph.addEdge(src, dest, weight)

    # Aplicar variaciones en el tiempo de retorno
    for variation, increment in variations:
        print(f"\n{variation}:")
        modified_graph = DirectedGraph()
        for src, dest, weight in edges:
            # Modificar los tiempos de retorno
            adjusted_weight = weight
            if src == 'D' and dest == 'A':  # Modificar solo el tiempo de retorno
                adjusted_weight += increment
            modified_graph.addEdge(src, dest, adjusted_weight)

        # Resolver TSP
        path, cost = modified_graph.tsp()
        print(f"Ruta óptima: {' -> '.join(path)} con costo {cost}")

demo_tsp()
