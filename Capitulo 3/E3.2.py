from SortArray import Array

# Crear una instancia de Array
maxSize = 10
array = Array(maxSize)

# Insertar elementos en el arreglo
array.insert(10)
array.insert(20)
array.insert(30)
array.insert(40)
array.insert(50)

# Mostrar contenido original
print("Contenido del arreglo:")
array.traverse()

# Calcular y mostrar la mediana
print("\nLa mediana del arreglo es:", array.mediana())

# Probar con número par de elementos
array.insert(60)
print("\nContenido del arreglo con número par de elementos:")
array.traverse()
print("La mediana del arreglo es:", array.mediana())

# Probar con un solo elemento
array_single = Array(maxSize)
array_single.insert(15)
print("\nContenido del arreglo con un solo elemento:")
array_single.traverse()
print("La mediana del arreglo es:", array_single.mediana())

# Probar con arreglo vacío
array_empty = Array(maxSize)
print("\nContenido del arreglo vacío:")
print("La mediana del arreglo vacío es:", array_empty.mediana())


Contenido del arreglo:
10
20
30
40
50

La mediana del arreglo es: 30

Contenido del arreglo con número par de elementos:
10
20
30
40
50
60
La mediana del arreglo es: 35.0

Contenido del arreglo con un solo elemento:
15
La mediana del arreglo es: 15

Contenido del arreglo vacío:
La mediana del arreglo vacío es: None
