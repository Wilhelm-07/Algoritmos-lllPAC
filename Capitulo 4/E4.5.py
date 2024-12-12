class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def delete_max(self):
        if self.is_empty():
            raise ValueError("La cola está vacía")
        max_index = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[max_index]:
                max_index = i
        item = self.items[max_index]
        del self.items[max_index]
        return item

    def __str__(self):
        return str(self.items)

        if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(5)
    pq.insert(2)

    print(pq)  # Salida: [3, 1, 5, 2]

    print(pq.delete_max())  # Imprime 5
    print(pq)  # Salida: [3, 1, 2]