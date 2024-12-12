import random

def insertion_sort(arr, low, high):
    copies = 0
    comparisons = 0
    for i in range(low + 1, high + 1):
        temp = arr[i]
        j = i - 1
        while j >= low and arr[j] > temp:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            copies += 1
        arr[j + 1] = temp
        copies += 1
    return comparisons, copies

def quicksort(arr, low, high, short):
    comparisons = 0
    copies = 0

    if low < high:
        if high - low + 1 <= short:  # Usa ordenamiento por inserción para subarreglos pequeños
            comp, cop = insertion_sort(arr, low, high)
            comparisons += comp
            copies += cop
        else:
            pivot, comp, cop = partition(arr, low, high)
            comparisons += comp
            copies += cop
            # Recursión
            comp_left, cop_left = quicksort(arr, low, pivot - 1, short)
            comp_right, cop_right = quicksort(arr, pivot + 1, high, short)
            comparisons += comp_left + comp_right
            copies += cop_left + cop_right

    return comparisons, copies

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    copies = 0

    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            copies += 3  # Cada intercambio cuenta como 3 copias

    # Intercambia pivot con el elemento correcto
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    copies += 3
    return i + 1, comparisons, copies

---

### Pruebas

```python
def test_quicksort():
    sizes = [3, 7, 11]  # Valores de "short" para subarreglos pequeños
    array_types = [
        ("Ordenada hacia adelante", list(range(1, 51))),
        ("Ordenada inversamente", list(range(50, 0, -1))),
        ("Constante", [5] * 50),
        ("Aleatoria", random.sample(range(1, 101), 50))
    ]

    for short in sizes:
        print(f"\n--- Pruebas con 'short' = {short} ---")
        for name, array in array_types:
            arr = array.copy()  # Copia para no modificar la matriz original
            comparisons, copies = quicksort(arr, 0, len(arr) - 1, short)
            print(f"{name}: Comparaciones = {comparisons}, Copias = {copies}")

test_quicksort()
