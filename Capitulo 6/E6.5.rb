def equipos(candidatos, k):
    """
    Encuentra todos los equipos posibles de tamaño k a partir de un grupo de candidatos.

    :param candidatos: Cadena que representa a las personas disponibles (ej. "ABTZ").
    :param k: Tamaño de los equipos.
    :return: Lista de cadenas que representan los diferentes equipos.
    """
    # Caso base: Si k es 0, devuelve un equipo vacío
    if k == 0:
        return [""]

    # Caso base: Si no hay candidatos suficientes para formar un equipo
    if len(candidatos) < k:
        return []

    # Dividir en dos opciones:
    # 1. Incluir el primer candidato en el equipo
    equipos_incluyendo = equipos(candidatos[1:], k - 1)
    equipos_incluyendo = [candidatos[0] + equipo for equipo in equipos_incluyendo]

    # 2. Excluir el primer candidato y buscar equipos en los candidatos restantes
    equipos_excluyendo = equipos(candidatos[1:], k)

    # Combinar ambas opciones
    return equipos_incluyendo + equipos_excluyendo


# Pruebas
candidatos = "ABTZ"
k = 2

print(f"Candidatos: {candidatos}")
print(f"Tamaño del equipo: {k}")
print("Equipos posibles:")
resultados = equipos(candidatos, k)
print(resultados)
