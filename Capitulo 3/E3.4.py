class Array:
    def __init__(self, maxSize):
        self.__a = [None] * maxSize  # Lista interna
        self.__nItems = 0           # Número de elementos actuales

    def __len__(self):
        return self.__nItems

    def insert(self, item):
        """Inserta un elemento al final del arreglo."""
        if self.__nItems >= len(self.__a):  # Verificar si hay espacio
            raise Exception("Array está lleno.")
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def traverse(self, function=print):
        """Recorre todos los elementos del arreglo."""
        for i in range(self.__nItems):
            function(self.__a[i])

    def oddEvenSort(self):
        """Realiza una ordenación par-impar en el arreglo."""
        sorted = False
        while not sorted:
            sorted = True

            # Primera pasada: ordenar los pares impares (j = 1, 3, 5, ...)
            for i in range(1, self.__nItems-1, 2):
                if self.__a[i] > self.__a[i+1]:
                    self.__a[i], self.__a[i+1] = self.__a[i+1], self.__a[i]
                    sorted = False

            # Segunda pasada: ordenar los pares pares (j = 0, 2, 4, ...)
            for i in range(0, self.__nItems-1, 2):
                if self.__a[i] > self.__a[i+1]:
                    self.__a[i], self.__a[i+1] = self.__a[i+1], self.__a[i]
                    sorted = False

    def oddEvenSortPasses(self):
        """Calcula el número máximo de pasadas necesarias para ordenar."""
        passes = 0
        while True:
            current_size = self.__nItems - 1
            new_size = 0

            # Perform an odd-even sort pass
            self.oddEvenSort()
            new_size = sum(1 for i in range(self.__nItems - 1) if self.__a[i] > self.__a[i+1])

            passes += 1
            if new_size == 0:  # No changes, array is sorted
                break

        return passes


from SortArray import Array

# Crear una instancia de Array
maxSize = 10
array = Array(maxSize)

# Insertar elementos en el arreglo
array.insert(37)
array.insert(10)
array.insert(25)
array.insert(44)
array.insert(15)
array.insert(90)
array.insert(80)
array.insert(12)
array.insert(5)
array.insert(60)

print("Contenido inicial del arreglo:")
array.traverse()

# Ordenar el arreglo usando el método oddEvenSort
array.oddEvenSort()

print("\nArreglo ordenado usando oddEvenSort:")
array.traverse()

# Determinar el número de pasadas necesarias
passes = array.oddEvenSortPasses()
print(f"\nNúmero máximo de pasadas necesarias: {passes}")

# Probar con un arreglo ya ordenado
array_sorted = Array(maxSize)
for i in range(maxSize):
    array_sorted.insert(i * 10)

print("\nArreglo ya ordenado:")
array_sorted.traverse()

# Usar oddEvenSort
array_sorted.oddEvenSort()

print("\nArreglo después de usar oddEvenSort:")
array_sorted.traverse()

# Determinar el número de pasadas necesarias para el arreglo ya ordenado
passes_sorted = array_sorted.oddEvenSortPasses()
print(f"\nNúmero máximo de pasadas necesarias para arreglo ya ordenado: {passes_sorted}")

# Probar con un arreglo desordenado
array_reverse = Array(maxSize)
for i in range(maxSize-1, -1, -1):
    array_reverse.insert(i * 10)

print("\nArreglo desordenado:")
array_reverse.traverse()

# Usar oddEvenSort
array_reverse.oddEvenSort()

print("\nArreglo después de usar oddEvenSort:")
array_reverse.traverse()

# Determinar el número de pasadas necesarias para el arreglo desordenado
passes_reverse = array_reverse.oddEvenSortPasses()
print(f"\nNúmero máximo de pasadas necesarias para arreglo desordenado: {passes_reverse}")
