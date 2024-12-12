class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Prueba del programa
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Lista después de agregar elementos:", ll.display())
ll.delete(20)
print("Lista después de eliminar 20:", ll.display())
print("Búsqueda de 30:", "Encontrado" if ll.search(30) else "No encontrado")
