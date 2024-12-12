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

    def move(self, old_row, old_col, new_row, new_col):
        """Mueve los datos de la posición antigua a una nueva posición."""
        old_key = (old_row, old_col)
        new_key = (new_row, new_col)

        if old_key not in self.grid or not self.grid[old_key]:
            return None

        # Mover los datos de la posición antigua a la nueva
        data_to_move = self.grid[old_key].pop()
        self.insert(new_row, new_col, data_to_move)

    def display(self):
        """Muestra los datos en la matriz."""
        for row in range(self.rows):
            for col in range(self.cols):
                key = (row, col)
                print(f"({row}, {col}): {self.grid.get(key, [])}")

# Ejemplo de uso
grid = Grid(5, 5)

# Insertar datos
grid.insert(2, 3, 'data1')
grid.insert(2, 3, 'data2')

# Mostrar la matriz actual
print("Matriz actual:")
grid.display()

# Mover datos
grid.move(2, 3, 4, 4)

# Mostrar la matriz después de mover los datos
print("\nMatriz después de mover los datos:")
grid.display()
