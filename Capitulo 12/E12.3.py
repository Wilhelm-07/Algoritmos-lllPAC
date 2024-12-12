class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = {}

    def insert(self, row, col, data):
        """Inserta datos en la posición especificada en la matriz."""
        key = (row, col)
        if key in self.grid:
            self.grid[key].append(data)
        else:
            self.grid[key] = [data]

    def delete(self, row, col, data=None):
        """Elimina los datos de la posición especificada en la matriz."""
        key = (row, col)
        if key in self.grid:
            if data is None:
                # Eliminar todos los datos en esa posición
                del self.grid[key]
            else:
                # Eliminar solo el dato especificado
                if data in self.grid[key]:
                    self.grid[key].remove(data)
                    if not self.grid[key]:
                        del self.grid[key]
                else:
                    return None
        else:
            return None

    def find(self, row, col):
        """Busca datos en la posición especificada en la matriz."""
        key = (row, col)
        return self.grid.get(key, [])

# Ejemplo de uso
grid = Grid(5, 5)

# Insertar datos duplicados
grid.insert(2, 3, 'data1')
grid.insert(2, 3, 'data2')
grid.insert(2, 3, 'data3')

# Eliminar un dato específico
removed_data = grid.delete(2, 3, 'data2')
if removed_data:
    print(f"Datos eliminados: {removed_data}")
else:
    print("Dato no encontrado.")

# Buscar todos los datos en una posición
found_data = grid.find(2, 3)
print(f"Datos encontrados en (2, 3): {found_data}")




class QuadTree:
    class Node:
        def __init__(self, bounds):
            self.bounds = bounds
            self.data = []  # Lista de datos en este nodo
            self.children = []

        def insert(self, data):
            """Inserta datos en este nodo."""
            self.data.append(data)

        def search(self, x, y):
            """Busca datos en este nodo. Devuelve todos los datos si los encuentra."""
            if self.bounds.contains(x, y):
                return self.data[:]

    def __init__(self, bounds):
        self.bounds = bounds
        self.root = self.Node(bounds)

    def insert(self, x, y, data):
        """Inserta datos en el quadtree en la posición (x, y)."""
        self.root.insert(data)

    def search(self, x, y):
        """Busca datos en el quadtree en la posición (x, y)."""
        return self.root.search(x, y)

# Ejemplo de uso
quad_tree = QuadTree(bounds)

# Insertar datos duplicados
quad_tree.insert(2, 3, 'data1')
quad_tree.insert(2, 3, 'data2')

# Buscar datos
found_data = quad_tree.search(2, 3)
print(f"Datos encontrados en (2, 3): {found_data}")
