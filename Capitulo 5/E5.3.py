class Deque:
    class Node:
        def __init__(self, data, prev_node=None, next_node=None):
            self.data = data
            self.prev = prev_node
            self.next = next_node

    def __init__(self):
        self.head = None  # Puntero al primer nodo
        self.tail = None  # Puntero al último nodo
        self.size = 0     # Tamaño del deque

    def isEmpty(self):
        """Devuelve True si el deque está vacío."""
        return self.size == 0

    def insertLeft(self, data):
        """Inserta un elemento en el lado izquierdo del deque."""
        new_node = self.Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insertRight(self, data):
        """Inserta un elemento en el lado derecho del deque."""
        new_node = self.Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def removeLeft(self):
        """Elimina y devuelve el elemento del lado izquierdo del deque."""
        if self.isEmpty():
            raise IndexError("Deque vacío, no se puede eliminar del lado izquierdo.")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return data

    def removeRight(self):
        """Elimina y devuelve el elemento del lado derecho del deque."""
        if self.isEmpty():
            raise IndexError("Deque vacío, no se puede eliminar del lado derecho.")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return data

    def peekLeft(self):
        """Devuelve el elemento del lado izquierdo sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("Deque vacío, no se puede hacer peek del lado izquierdo.")
        return self.head.data

    def peekRight(self):
        """Devuelve el elemento del lado derecho sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("Deque vacío, no se puede hacer peek del lado derecho.")
        return self.tail.data

    def __len__(self):
        """Devuelve el tamaño del deque."""
        return self.size

    def traverse(self):
        """Recorre el deque desde el lado izquierdo al derecho."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Crear un deque
deque = Deque()

# Insertar elementos
deque.insertLeft(10)
deque.insertRight(20)
deque.insertLeft(5)
deque.insertRight(25)

# Recorrer el deque
print("Deque después de inserciones:")
deque.traverse()

# Operaciones de peek
print("Peek izquierda:", deque.peekLeft())  # Esperado: 5
print("Peek derecha:", deque.peekRight())  # Esperado: 25

# Eliminar elementos
print("Eliminar izquierda:", deque.removeLeft())  # Esperado: 5
print("Eliminar derecha:", deque.removeRight())  # Esperado: 25

# Recorrer el deque después de eliminaciones
print("Deque después de eliminaciones:")
deque.traverse()

# Verificar si está vacío
print("¿El deque está vacío?", deque.isEmpty())

# Tamaño del deque
print("Tamaño del deque:", len(deque))
