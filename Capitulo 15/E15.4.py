class WeightedDiGraph:
    # ... (rest of the class)

    def critical_path(self, start):
        def dfs(node, visited):
            if node in visited:
                return float('inf'), []  # Ciclo detectado
            visited.add(node)
            max_path = (0, [node])
            for neighbor, weight in self.graph.get(node, {}).items():
                path_len, path = dfs(neighbor, visited)
                if path_len + weight > max_path[0]:
                    max_path = (path_len + weight, path + [node])
            return max_path

        return dfs(start, set())

# Ejemplo de uso:
graph = WeightedDiGraph()
# ... (agregar aristas con pesos)
critical_path, total_time = graph.critical_path('A')
print("Camino crítico:", critical_path)
print("Tiempo total:", total_time)