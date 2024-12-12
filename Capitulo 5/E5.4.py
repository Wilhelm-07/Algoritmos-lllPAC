class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        class CircularLinkedList:
    def __init__(self):
        self.last = None

    def is_empty(self):
        return self.last is None

    def first(self):
        if self.is_empty():
            raise ValueError("Lista vacía")
        return self.last.next.data

    def insert_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Lista vacía")
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def search(self, key):
        if self.is_empty():
            return None
        current = self.last.next
        while current != self.last:
            if current.data == key:
                return current.data
            current = current.next
        if current.data == key:
            return current.data
        return None

    def step(self):
        if self.is_empty():
            raise ValueError("Lista vacía")
        self.last = self.last.next

    def seek(self, key):
        if self.is_empty():
            return None
        current = self.last.next
        while current != self.last:
            if current.data == key:
                self.last = current
                return current.data
            current = current.next
        if current.data == key:
            self.last = current
            return current.data
        return None

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "["
        current = self.last.next
        while True:
            result += str(current.data)
            current = current.next
            if current == self.last.next:
                break
            result += ", "
        return result + "]"