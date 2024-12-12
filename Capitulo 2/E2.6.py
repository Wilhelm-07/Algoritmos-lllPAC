class OrderedRecordArray:
    def __init__(self, maxSize):
        self.__a = [None] * maxSize  # Lista interna
        self.__nItems = 0           # Número de elementos en la lista

    def __len__(self):
        return self.__nItems

    def insert(self, item):
        """Inserta un elemento en el orden correcto."""
        if self.__nItems >= len(self.__a):  # Verifica si hay espacio
            raise Exception("Array está lleno.")

        j = 0
        while j < self.__nItems and self.__a[j] < item:  # Encuentra la posición
            j += 1

        for k in range(self.__nItems, j, -1):  # Desplaza elementos hacia la derecha
            self.__a[k] = self.__a[k - 1]

        self.__a[j] = item  # Inserta el elemento
        self.__nItems += 1

    def find(self, key):
        """Realiza una búsqueda binaria para encontrar el índice de una clave."""
        lower = 0
        upper = self.__nItems - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if self.__a[mid] < key:
                lower = mid + 1
            elif self.__a[mid] > key:
                upper = mid - 1
            else:
                return mid  # Encuentra el índice

        return -1  # No se encuentra la clave

    def search(self, key):
        """Busca una clave y devuelve su valor."""
        index = self.find(key)
        return self.__a[index] if index != -1 else None

    def delete(self, key):
        """Elimina todas las instancias de una clave si está presente."""
        index = self.find(key)

        if index == -1:  # Clave no encontrada
            return False

        # Busca hacia la izquierda para encontrar duplicados
        start = index
        while start > 0 and self.__a[start - 1] == key:
            start -= 1

        # Busca hacia la derecha para encontrar duplicados
        end = index
        while end < self.__nItems - 1 and self.__a[end + 1] == key:
            end += 1

        # Calcula cuántos elementos se eliminarán
        num_to_delete = end - start + 1

        # Desplaza los elementos hacia la izquierda
        for i in range(start, self.__nItems - num_to_delete):
            self.__a[i] = self.__a[i + num_to_delete]

        self.__nItems -= num_to_delete  # Reduce el tamaño lógico del arreglo
        return True

    def traverse(self, function=print):
        """Recorre todos los elementos del arreglo."""
        for i in range(self.__nItems):
            function(self.__a[i])


from OrderedRecordArray import OrderedRecordArray

# Crear una instancia de OrderedRecordArray
maxSize = 20
array = OrderedRecordArray(maxSize)

# Insertar elementos, incluyendo claves duplicadas
array.insert(10)
array.insert(20)
array.insert(20)
array.insert(30)
array.insert(40)
array.insert(20)
array.insert(50)

# Mostrar el contenido original
print("Contenido original:")
array.traverse()

# Prueba de eliminación: Clave con duplicados
print("\nEliminando la clave '20' (con duplicados):")
array.delete(20)
array.traverse()

# Prueba de eliminación: Clave sin duplicados
print("\nEliminando la clave '30':")
array.delete(30)
array.traverse()

# Prueba de eliminación: Clave inexistente
print("\nIntentando eliminar la clave '60' (no existente):")
result = array.delete(60)
print("Resultado de la eliminación:", result)
array.traverse()

# Prueba con un solo elemento duplicado
print("\nInsertando claves duplicadas nuevamente:")
array.insert(50)
array.insert(50)
array.insert(50)
print("Contenido antes de eliminar '50':")
array.traverse()
print("Eliminando '50':")
array.delete(50)
array.traverse()

# Prueba con array vacío
print("\nPrueba con un array vacío:")
empty_array = OrderedRecordArray(maxSize)
result = empty_array.delete(10)
print("Resultado de la eliminación en array vacío:", result)


Contenido original:
10
20
20
20
30
40
50

Eliminando la clave '20' (con duplicados):
10
30
40
50

Eliminando la clave '30':
10
40
50

Intentando eliminar la clave '60' (no existente):
Resultado de la eliminación: False
10
40
50

Insertando claves duplicadas nuevamente:
Contenido antes de eliminar '50':
10
40
50
50
50
Eliminando '50':
10
40

Prueba con un array vacío:
Resultado de la eliminación en array vacío: False
