def mult(x, y):
    """Multiplica dos números enteros usando solo suma de forma recursiva.

    Args:
        x: Primer número entero.
        y: Segundo número entero.

    Returns:
        El producto de x e y.
    """

    if y == 0:
        return 0  # Caso base: cualquier número multiplicado por 0 es 0
    elif y > 0:
        return x + mult(x, y - 1)  # Suma x a sí mismo y-1 veces
    else:
        return -mult(x, -y)  # Si y es negativo, invertimos el signo y llamamos recursivamente