class BulkQuadTree(QuadTree):
    def __init__(self, points, boundaries):
        super().__init__(boundaries)
        self.bulk_insert(points)

    def bulk_insert(self, points):
        def _bulk_insert(node, points):
            if not points:
                return
            if all(child is None for child in node.children):
                # Nodo hoja, distribuir los puntos entre los hijos
                for point in points:
                    self.insert(node, point)
            else:
                # Dividir los puntos entre los hijos
                for child_index, child in enumerate(node.children):
                    child_points = [p for p in points if p in child.boundaries]
                    _bulk_insert(child, child_points)

        _bulk_insert(self.root, points)

    def measure_balance(self):
        # Implementación para medir el equilibrio del árbol
        # Por ejemplo, se puede calcular la diferencia de altura entre los subárboles
        # o contar el número de nodos en cada nivel

def measure_bulk_insertion(points, boundaries):
    # Crear un BulkQuadTree
    tree = BulkQuadTree(points, boundaries)
    # Medir el equilibrio del árbol
    balance = tree.measure_balance()
    return balance

# Ejemplo de uso
points = [(x, y) for x in range(100) for y in range(100)]  # Generar puntos aleatorios
boundaries = (0, 0, 100, 100)
tree = BulkQuadTree(points, boundaries)
balance = measure_bulk_insertion(points, boundaries)
print("Balance del árbol:", balance)