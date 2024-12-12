class Node:
    def __init__(self, data, boundaries):
        self.data = data
        self.boundaries = boundaries
        self.children = [None, None, None, None]

class QuadTree:
    def __init__(self, boundaries):
        self.root = Node(None, boundaries)

    def insert(self, point):
        # ... (implementación existente)

    def query(self, region):
        # ... (implementación existente)

    def delete(self, point):
        def _delete(node, point):
            if node is None:
                return None
            if node.data is None:
                # Nodo ya eliminado
                return node

            # Verificar si el punto está dentro de las fronteras del nodo
            if point in node.boundaries:
                # Si el nodo es una hoja y coincide con el punto, marcarlo como eliminado
                if all(child is None for child in node.children):
                    node.data = None
                    return node
                else:
                    # Buscar en los subárboles
                    for i in range(4):
                        if point in node.children[i].boundaries:
                            node.children[i] = _delete(node.children[i], point)
                            break
            return node

        self.root = _delete(self.root, point)