class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data, key):
        new_node = Node(data, key)
        if self.is_empty() or new_node.key < self.head.key:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.key < new_node.key:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_min(self):
        if self.is_empty():
            raise ValueError("La cola está vacía")
        min_node = self.head
        self.head = self.head.next
        return min_node.data


        pq = PriorityQueue()
pq.insert("task1", 2)
pq.insert("task3", 1)
pq.insert("task2", 3)

print(pq.delete_min())  # Imprime "task3"
print(pq.delete_min())  # Imprime "task1"
print(pq.delete_min())  # Imprime "task2"