def contar_palabras(archivo):
    """Cuenta las palabras en un archivo de texto y devuelve un diccionario con las frecuencias.

    Args:
        archivo (str): Nombre del archivo de texto.

    Returns:
        dict: Un diccionario donde las claves son las palabras y los valores son las frecuencias.
    """

    frecuencias = {}
    with open(archivo, 'r') as f:
        for linea in f:
            for palabra in linea.split():
                palabra = palabra.strip('()<>[]{}-_,.?!:;"').lower()
                frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

if __name__ == "__main__":
    archivo = "mi_archivo.txt"  # Reemplaza con el nombre de tu archivo
    resultado = contar_palabras(archivo)

    for palabra, frecuencia in resultado.items():
        print(f"{palabra}: {frecuencia}")