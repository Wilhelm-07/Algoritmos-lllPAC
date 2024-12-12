from deque import Deque  # Suponiendo que Deque está en un módulo llamado deque

class Stack:
    def __init__(self):
        self.items = Deque()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.insert_right(item)

    def pop(self):
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self.items.delete_right()

    def peek(self):
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self.items.peek_right()

        stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Imprime 3
print(stack.peek())  # Imprime 2