import random

def shell_sort(arr, gap_sequence):
    """
    Implementa el algoritmo ShellSort con una secuencia de intervalos personalizada.

    Args:
        arr: Lista a ordenar.
        gap_sequence: Generador de la secuencia de intervalos.
    """
    for gap in gap_sequence:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

def knuth_sequence(n):
    """Genera la secuencia de intervalos de Knuth."""
    gaps = []
    h = 1
    while h <= n // 3:
        gaps.append(h)
        h = 3 * h + 1
    gaps.reverse()
    return gaps

def divide_by_2_2(n):
    """Genera la secuencia de intervalos dividiendo por 2.2 y truncando."""
    gaps = []
    h = n
    while h > 1:
        gaps.append(h)
        h = int(h / 2.2)
    return gaps

def flamings_sequence(n):
    """Genera la secuencia de intervalos de Flamig."""
    gaps = []
    h = 1
    while h <= n / 3:
        gaps.append(h)
        h = 2 * h + 1
    gaps.reverse()
    return gaps

# Función para generar una matriz aleatoria
def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

# Función para contar el número de intercambios
def count_swaps(arr, gap_sequence):
    swaps = 0
    # ... (código de ShellSort con contador de intercambios)
    return swaps

# Comparación de las secuencias
for size in range(95, 101):
    # Generar matrices ordenada, inversamente ordenada y aleatoria
    sorted_arr = list(range(size))
    reversed_arr = sorted_arr[::-1]
    random_arr = generate_random_array(size)

    for arr in [sorted_arr, reversed_arr, random_arr]:
        print(f"Tamaño de la matriz: {size}")
        for sequence in [knuth_sequence, divide_by_2_2, flamings_sequence]:
            arr_copy = arr.copy()
            swaps = count_swaps(arr_copy, sequence(size))
            print(f"  {sequence.__name__}: {swaps} intercambios")