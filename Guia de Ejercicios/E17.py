class LinkedList:
    # Clase y métodos previos...
    # Append, delete, search, display aquí...

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Prueba del método reverse()
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Lista original:", ll.display())
ll.reverse()
print("Lista invertida:", ll.display())
