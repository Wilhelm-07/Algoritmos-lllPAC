def __growTable(self):
    new_size = self.size * 2
    new_table = [None] * new_size
    for key, value in self.items:
        new_index = hash(key) % new_size
        # ... (resto del código para reubicar los elementos)