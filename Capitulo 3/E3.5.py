class Array:
    def __init__(self, maxSize):
        self.__a = [None] * maxSize
        self.__nItems = 0
        self.copias = 0
        self.comparaciones = 0

    def __len__(self):
        return self.__nItems

    def insert(self, item):
        """Inserta un elemento al final del arreglo."""
        if self.__nItems >= len(self.__a):
            raise Exception("Array está lleno.")
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def traverse(self, function=print):
        """Recorre todos los elementos del arreglo."""
        for i in range(self.__nItems):
            function(self.__a[i])

    def insertionSort(self):
        """Ordenación por inserción, contando copias y comparaciones."""
        self.copias = 0
        self.comparaciones = 0

        for i in range(1, self.__nItems):
            current_value = self.__a[i]
            j = i - 1
            while j >= 0 and self.__a[j] > current_value:
                self.comparaciones += 1  # Contar comparaciones
                self.__a[j + 1] = self.__a[j]  # Copiar elemento
                self.copias += 1
                j -= 1
            self.__a[j + 1] = current_value  # Colocar el valor de vuelta
            self.copias += 1

    def insertionSortMetrics(self):
        """Imprime las métricas de copias y comparaciones realizadas durante la clasificación."""
        print(f"Copias realizadas: {self.copias}")
        print(f"Comparaciones realizadas: {self.comparaciones}")


from SortArray import Array

# Crear una instancia de Array
maxSize = 10
array_sorted = Array(maxSize)

# Insertar elementos ordenados
for i in range(maxSize):
    array_sorted.insert(i)

print("Datos ordenados:")
array_sorted.insertionSort()
array_sorted.insertionSortMetrics()

# Insertar elementos en orden inverso
array_reverse = Array(maxSize)
for i in range(maxSize-1, -1, -1):
    array_reverse.insert(i)

print("\nDatos en orden inverso:")
array_reverse.insertionSort()
array_reverse.insertionSortMetrics()

# Insertar elementos casi ordenados (últimos dos fuera de lugar)
array_nearly_sorted = Array(maxSize)
for i in range(maxSize - 2):
    array_nearly_sorted.insert(i)
array_nearly_sorted.insert(9)  # Estos dos elementos están fuera de lugar
array_nearly_sorted.insert(7)

print("\nDatos casi ordenados:")
array_nearly_sorted.insertionSort()
array_nearly_sorted.insertionSortMetrics()
