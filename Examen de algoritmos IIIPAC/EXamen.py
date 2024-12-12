class ColaEspacial:
    def __init__(self, tamano):
        self.cola = [None] * tamano
        self.inicio = 0
        self.final = -1
        self.tamano = tamano

    def insertar(self, elemento):
        if self.final == self.tamano - 1:  # Si la cola está llena
            self.final = self.inicio  # El final se convierte en el inicio
        else:
            self.final += 1
        self.cola[self.final] = elemento

    def mostrar(self):
        print(self.cola)
        
        from ColaEspacial import ColaEspacial

if __name__ == "__main__":
    cola = ColaEspacial(10)
    elementos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for elemento in elementos:
        cola.insertar(elemento)
        cola.mostrar()
        
        from ColaEspacial import ColaEspacial

if __name__ == "__main__":
    cola = ColaEspacial(10)
    elementos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for elemento in elementos:
        cola.insertar(elemento)
        cola.mostrar()
        if __name__ == "__main__":
    cola = ColaEspacial(10)
    elementos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for elemento in elementos:
        cola.insertar(elemento)
        cola.mostrar()

    # Eliminar algunos elementos
    for _ in range(5):
        cola.eliminar()
        cola.mostrar()

    # Insertar más elementos
    for elemento in "12345":
        cola.insertar(elemento)
        cola.mostrar()