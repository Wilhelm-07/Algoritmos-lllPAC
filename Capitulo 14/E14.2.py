class Graph:
    # ... (resto de la clase Graph)

    def depthFirstR(self, start):
        visited = set()  # Conjunto para marcar nodos visitados
        stack = [start]  # Pila implícita a través de la recursión

        def dfs(node):
            visited.add(node)
            yield node  # Generar el nodo actual
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    yield from dfs(neighbor)  # Recursión y delegación de generación

        yield from dfs(start)