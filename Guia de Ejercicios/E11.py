def invertir(self):
    prev = None
    actual = self.head
    while actual:
        siguiente = actual.next
        actual.next = prev
        prev = actual
        actual = siguiente
    self.head = prev