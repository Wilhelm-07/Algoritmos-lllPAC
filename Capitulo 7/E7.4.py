def radix_sort(arr, base=10):
    max_val = max(arr)  # Determina el valor máximo
    max_digits = len(str(max_val))  # Calcula la cantidad de dígitos en la clave más larga
    copies = 0

    # Itera sobre cada posición del dígito
    for digit in range(max_digits):
        # Crea contenedores (buckets) para cada valor posible en la base
        buckets = [[] for _ in range(base)]

        # Distribuye los números en los contenedores según el dígito actual
        for num in arr:
            digit_val = (num // (base ** digit)) % base
            buckets[digit_val].append(num)
            copies += 1

        # Reconstruye el arreglo desde los contenedores
        arr = [num for bucket in buckets for num in bucket]
        copies += len(arr)  # Cada número se copia de los buckets al arreglo principal

    return arr, copies

---

### Pruebas

```python
import random

def test_radix_sort():
    test_cases = [
        ("Claves hasta 99", [random.randint(0, 99) for _ in range(50)]),
        ("Claves hasta 999", [random.randint(0, 999) for _ in range(50)]),
    ]

    for name, array in test_cases:
        print(f"\n--- {name} ---")
        print("Matriz original:", array)
        sorted_array, copies = radix_sort(array, base=10)
        print("Matriz ordenada:", sorted_array)
        print("Copias realizadas:", copies)

test_radix_sort()
