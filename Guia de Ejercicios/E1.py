def suma_arreglo(arreglo):
  """Calcula la suma de todos los elementos de un arreglo.

  Args:
    arreglo: Un arreglo de números.

  Returns:
    La suma de todos los elementos del arreglo.
  """

  suma = 0
  for numero in arreglo:
    suma += numero
  return suma

# Ejemplo de uso:
mi_arreglo = [1, 2, 3, 4, 5]
resultado = suma_arreglo(mi_arreglo)
print("La suma de los elementos es:", resultado)