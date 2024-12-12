class Array:
    def __init__(self, initialSize):
        self.__a = [None] * initialSize  # El arreglo se almacena como una lista
        self.__nItems = 0  # Número inicial de elementos en la matriz

    def __len__(self):
        return self.__nItems  # Retorna la cantidad de elementos

    def get(self, n):
        if 0 <= n < self.__nItems:  # Verifica límites
            return self.__a[n]
        return None

    def set(self, n, value):
        if 0 <= n < self.__nItems:  # Verifica límites
            self.__a[n] = value

    def insert(self, item):
        if self.__nItems < len(self.__a):  # Asegúrate de que haya espacio
            self.__a[self.__nItems] = item
            self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        index = self.find(item)
        return self.get(index) if index != -1 else None

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:  # Elemento encontrado
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]  # Desplaza elementos hacia la izquierda
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def removeDupes(self):
        """Elimina valores duplicados del arreglo."""
        seen = set()
        new_array = []

        for i in range(self.__nItems):
            if self.__a[i] not in seen:  # Agrega solo si no está duplicado
                seen.add(self.__a[i])
                new_array.append(self.__a[i])

        # Actualiza el arreglo con los elementos únicos
        self.__nItems = len(new_array)
        self.__a[:self.__nItems] = new_array  # Copia los valores únicos al arreglo original


import Array

# Crea una instancia de la clase Array
maxSize = 15
arr = Array.Array(maxSize)

# Inserta elementos, incluyendo duplicados
arr.insert(10)
arr.insert(20)
arr.insert(10)
arr.insert(30)
arr.insert(20)
arr.insert(40)
arr.insert("foo")
arr.insert("bar")
arr.insert("foo")
arr.insert(50)
arr.insert("baz")

# Muestra el contenido original
print("Array original:")
arr.traverse()

# Prueba removeDupes
print("\nEliminando duplicados...")
arr.removeDupes()

# Muestra el contenido tras eliminar duplicados
print("Array después de eliminar duplicados:")
arr.traverse()

# Pruebas adicionales: array sin duplicados
print("\nPrueba con matriz sin duplicados:")
arr_no_dupes = Array.Array(maxSize)
arr_no_dupes.insert(1)
arr_no_dupes.insert(2)
arr_no_dupes.insert(3)
print("Matriz original:")
arr_no_dupes.traverse()
arr_no_dupes.removeDupes()
print("Matriz después de removeDupes:")
arr_no_dupes.traverse()

# Pruebas adicionales: array vacío
print("\nPrueba con matriz vacía:")
arr_empty = Array.Array(maxSize)
print("Matriz original:")
arr_empty.traverse()
arr_empty.removeDupes()
print("Matriz después de removeDupes:")
arr_empty.traverse()


Array original:
10
20
10
30
20
40
foo
bar
foo
50
baz

Eliminando duplicados...
Array después de eliminar duplicados:
10
20
30
40
foo
bar
50
baz

Prueba con matriz sin duplicados:
Matriz original:
1
2
3
Matriz después de removeDupes:
1
2
3

Prueba con matriz vacía:
Matriz original:
Matriz después de removeDupes:
