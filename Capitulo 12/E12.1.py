class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = {}

    def insert(self, row, col, data):
        """Inserta datos en la posición especificada en la matriz."""
        if (row, col) not in self.grid:
            self.grid[(row, col)] = data
        else:
            raise ValueError("La celda ya contiene datos.")

    def delete(self, row, col):
        """Elimina los datos de la posición especificada en la matriz."""
        key = (row, col)
        if key in self.grid:
            data = self.grid.pop(key)
            return data
        else:
            return None

# Ejemplo de uso
grid = Grid(5, 5)  # Crea una cuadrícula de 5x5

# Insertar algunos puntos
grid.insert(2, 3, 'data1')
grid.insert(4, 1, 'data2')

# Eliminar un punto existente
data_removed = grid.delete(2, 3)
if data_removed:
    print(f"Datos eliminados: {data_removed}")
else:
    print("Punto no encontrado.")

# Intentar eliminar un punto no existente
data_removed = grid.delete(1, 1)
if data_removed:
    print(f"Datos eliminados: {data_removed}")
else:
    print("Punto no encontrado.")
