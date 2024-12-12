class Deque:
    def __init__(self, maxlen):
        self.items = [None] * maxlen
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxlen = maxlen

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxlen

    def insert_left(self, item):
        if self.is_full():
            raise Exception("Deque está lleno")
        self.front = (self.front - 1) % self.maxlen
        self.items[self.front] = item
        self.size += 1

    def insert_right(self, item):
        if self.is_full():
            raise Exception("Deque está lleno")
        self.rear = (self.rear + 1) % self.maxlen
        self.items[self.rear] = item
        self.size += 1

    def delete_left(self):
        if self.is_empty():
            raise Exception("Deque está vacío")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.maxlen
        self.size -= 1
        return item

    def delete_right(self):
        if self.is_empty():
            raise Exception("Deque está vacío")
        item = self.items[self.rear]
        self.rear = (self.rear - 1) % self.maxlen
        self.size -= 1
        return item

    def peek_left(self):
        if self.is_empty():
            raise Exception("Deque está vacío")
        return self.items[self.front]

    def peek_right(self):
        if self.is_empty():
            raise Exception("Deque está vacío")
        return self.items[self.rear]