def power(x, y):
    """
    Calcula x^y usando un enfoque recursivo.
    
    :param x: Base (número).
    :param y: Exponente (entero, puede ser negativo).
    :return: Resultado de x^y.
    """
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if y == 0:
        return 1
    # Caso base: cualquier número elevado a la potencia 1 es sí mismo
    elif y == 1:
        return x
    # Caso de exponente negativo
    elif y < 0:
        return 1 / power(x, -y)
    # Caso recursivo: multiplicar x por x^(y-1)
    else:
        return x * power(x, y - 1)

# Pruebas
print(power(2, 3))   # 8 (2^3)
print(power(5, -2))  # 0.04 (5^-2)
print(power(7, 0))   # 1 (7^0)
print(power(3, 1))   # 3 (3^1)
print(power(-2, 3))  # -8 (-2^3)
print(power(2, -3))  # 0.125 (2^-3)
