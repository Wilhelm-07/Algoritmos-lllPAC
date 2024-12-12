class Graph:
    # ... (resto de la clase Graph)

    def breadthFirst(self, start):
        visited = {start: None}  # Diccionario para almacenar el nodo padre
        queue = [start]

        while queue:
            node = queue.pop(0)
            yield node, visited[node]  # Generar el nodo y su padre
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)

    def shortestPath(self, start, end):
        path = []
        for node, parent in self.breadthFirst(start):
            if node == end:
                while node is not None:
                    path.append(node)
                    node = parent
                return path[::-1]  # Invertir el camino
        return None  # No existe camino

# Ejemplo de uso con los grafos de la Figura 14-10 y 14-14
# ... (Suponiendo que los grafos están definidos)

# Camino más corto de A a H en el grafo de la Figura 14-10
path = graph2.shortestPath('A', 'H')
if path:
    print("Camino más corto de A a H:", path)
else:
    print("No existe camino de A a H")

# Camino más corto de F a A en el grafo de la Figura 14-14
path = graph1.shortestPath('F', 'A')
# ... (similar al caso anterior)