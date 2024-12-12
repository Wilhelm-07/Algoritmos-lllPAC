class WeightedGraph:
    # ... (rest of the class)

    def connected_components(self, threshold=float('inf')):
        labels = {vertex: vertex for vertex in self.graph}

        def update_labels(labels, edge):
            u, v, weight = edge
            if weight <= threshold and labels[u] != labels[v]:
                if labels[u] < labels[v]:
                    labels[v] = labels[u]
                else:
                    labels[u] = labels[v]

        # Repeatedly update labels until no more changes
        changed = True
        while changed:
            changed = False
            for edge in self.edges():
                changed |= update_labels(labels, edge)

        return labels

    def component_vertices(self, labels):
        components = {}
        for vertex, label in labels.items():
            if label not in components:
                components[label] = []
            components[label].append(vertex)
        return components

# Example usage:
# ... (create a graph as shown in Figure 15-21)

labels_50 = graph.connected_components(50)
components_50 = graph.component_vertices(labels_50)

# ... (similarly for thresholds 21 and 15)