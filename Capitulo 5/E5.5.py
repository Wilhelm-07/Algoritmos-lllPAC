class CircularList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.tail = None  # Nodo final que apunta al inicio
        self.size = 0

    def isEmpty(self):
        """Devuelve True si la lista está vacía."""
        return self.size == 0

    def insertAtEnd(self, data):
        """Inserta un nodo al final de la lista circular."""
        new_node = self.Node(data)
        if self.isEmpty():
            new_node.next = new_node  # Apunta a sí mismo
            self.tail = new_node
        else:
            new_node.next = self.tail.next  # Conecta al primer nodo
            self.tail.next = new_node      # Conecta al nuevo nodo
            self.tail = new_node           # Actualiza el nodo final
        self.size += 1

    def removeFromStart(self):
        """Elimina y devuelve el nodo desde el inicio de la lista circular."""
        if self.isEmpty():
            raise IndexError("La lista circular está vacía.")
        head = self.tail.next
        if self.size == 1:
            self.tail = None  # La lista queda vacía
        else:
            self.tail.next = head.next  # Salta al primer nodo
        self.size -= 1
        return head.data

    def peekStart(self):
        """Devuelve el valor del primer nodo sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("La lista circular está vacía.")
        return self.tail.next.data

    def peekEnd(self):
        """Devuelve el valor del último nodo sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("La lista circular está vacía.")
        return self.tail.data

    def __len__(self):
        """Devuelve el tamaño de la lista circular."""
        return self.size


class CircularStack:
    def __init__(self):
        self.circular_list = CircularList()

    def push(self, data):
        """Inserta un elemento en la pila."""
        self.circular_list.insertAtEnd(data)

    def pop(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if self.circular_list.isEmpty():
            raise IndexError("La pila está vacía.")
        # Recorremos hasta el penúltimo nodo
        current = self.circular_list.tail.next  # Primer nodo
        prev = self.circular_list.tail          # Último nodo
        while current != self.circular_list.tail:
            prev = current
            current = current.next
        # Actualizamos la lista
        prev.next = current.next
        self.circular_list.tail = prev
        self.circular_list.size -= 1
        return current.data

    def peek(self):
        """Devuelve el elemento en la cima de la pila sin eliminarlo."""
        return self.circular_list.peekEnd()

    def isEmpty(self):
        """Devuelve True si la pila está vacía."""
        return self.circular_list.isEmpty()

    def __len__(self):
        """Devuelve el tamaño de la pila."""
        return len(self.circular_list)


class CircularQueue:
    def __init__(self):
        self.circular_list = CircularList()

    def insert(self, data):
        """Inserta un elemento en la cola."""
        self.circular_list.insertAtEnd(data)

    def remove(self):
        """Elimina y devuelve el elemento al frente de la cola."""
        return self.circular_list.removeFromStart()

    def peek(self):
        """Devuelve el elemento al frente de la cola sin eliminarlo."""
        return self.circular_list.peekStart()

    def isEmpty(self):
        """Devuelve True si la cola está vacía."""
        return self.circular_list.isEmpty()

    def __len__(self):
        """Devuelve el tamaño de la cola."""
        return len(self.circular_list)



# Probar la pila
stack = CircularStack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Pila después de push:", stack.peek())  # Esperado: 30
print("Pop de la pila:", stack.pop())        # Esperado: 30
print("Pila después de pop:", stack.peek())  # Esperado: 20

# Probar la cola
queue = CircularQueue()
queue.insert(10)
queue.insert(20)
queue.insert(30)
print("Cola después de insert:", queue.peek())  # Esperado: 10
print("Remove de la cola:", queue.remove())     # Esperado: 10
print("Cola después de remove:", queue.peek())  # Esperado: 20
