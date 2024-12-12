class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar_final(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def eliminar(self, data):
        # ... (implementación similar a la respuesta anterior)

    def buscar(self, data):
        # ... (implementación similar a la respuesta anterior)