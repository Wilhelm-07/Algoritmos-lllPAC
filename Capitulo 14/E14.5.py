class Graph:
    # ... (rest of the Graph class)

    def find_cliques(self, N):
        def is_clique(vertices):
            for i in range(len(vertices)):
                for j in range(i + 1, len(vertices)):
                    if vertices[i] not in self.neighbors(vertices[j]):
                        return False
            return True

        def find_cliques_recursive(vertices, clique):
            if len(clique) == N:
                yield clique
            else:
                for vertex in vertices:
                    new_clique = clique + [vertex]
                    if is_clique(new_clique):
                        yield from find_cliques_recursive(vertices - set(new_clique), new_clique)

        cliques = []
        for vertex in self.vertices:
            cliques.extend(find_cliques_recursive(self.vertices - {vertex}, [vertex]))
        return cliques

# Example usage:
graph = Graph()
# ... (populate the graph with edges)

cliques_of_size_3 = graph.find_cliques(3)
cliques_of_size_4 = graph.find_cliques(4)