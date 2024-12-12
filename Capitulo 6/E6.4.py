def knapsack(target_weight, weights, index=0, current_combination=None):
    """
    Encuentra combinaciones de pesos que suman al peso objetivo utilizando recursión.

    :param target_weight: Peso objetivo (entero).
    :param weights: Lista de pesos disponibles.
    :param index: Índice desde donde empezar en la lista de pesos.
    :param current_combination: Lista que almacena la combinación actual de pesos.
    :return: Ninguno. Imprime las combinaciones que cumplen la condición.
    """
    if current_combination is None:
        current_combination = []

    # Caso base: si el peso objetivo es exactamente 0, imprime la combinación actual
    if target_weight == 0:
        print("Combinación encontrada:", current_combination)
        return

    # Caso base: si el peso objetivo es negativo o no quedan elementos, detener
    if target_weight < 0 or index >= len(weights):
        return

    # Incluye el peso actual en la combinación
    knapsack(target_weight - weights[index], weights, index + 1, current_combination + [weights[index]])

    # Excluye el peso actual y pasa al siguiente
    knapsack(target_weight, weights, index + 1, current_combination)

# Pruebas
weights = [1, 3, 4, 5]
target_weight = 7

print(f"Pesos disponibles: {weights}")
print(f"Peso objetivo: {target_weight}")
knapsack(target_weight, weights)
