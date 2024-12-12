def eliminar_duplicados(self):
    actual = self.head
    while actual:
        corredor = actual.next
        prev = actual
        while corredor:
            if corredor.data == actual.data:
                prev.next = corredor.next
                corredor = corredor.next
            else:
                prev = corredor
                corredor = corredor.next
        actual = actual.next