def knapsack(target_weight, weights, start_index, memo={}):
    """
    Resuelve el problema de la mochila de forma recursiva con memorización.

    Args:
        target_weight: Peso máximo que puede soportar la mochila.
        weights: Lista de pesos de los objetos.
        start_index: Índice inicial en la lista de pesos a considerar.
        memo: Diccionario para almacenar resultados calculados previamente.

    Returns:
        Una lista de listas, donde cada lista interna representa una combinación de pesos que suman el peso objetivo.
    """

    if (target_weight, start_index) in memo:
        return memo[(target_weight, start_index)]

    results = []
    if target_weight == 0:
        return [[]]
    if target_weight < 0 or start_index >= len(weights):
        return []

    # Incluir el elemento actual en la solución
    with_current = knapsack(target_weight - weights[start_index], weights, start_index + 1, memo)
    for combo in with_current:
        results.append([weights[start_index]] + combo)

    # No incluir el elemento actual en la solución
    without_current = knapsack(target_weight, weights, start_index + 1, memo)
    results.extend(without_current)

    memo[(target_weight, start_index)] = results
    return results

# Ejemplo de uso
weights = [2, 3, 6, 7]
target_weight = 7

solutions = knapsack(target_weight, weights, 0)
print(solutions)