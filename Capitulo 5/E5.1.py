class LinkedList:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traverse(self, function=print):
        for data in self:
            function(data)

    def __str__(self):
        return " -> ".join(str(data) for data in self)

    def __len__(self):
        return sum(1 for _ in self)

    # Métodos para añadir nodos (para pruebas)
    def insert(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

