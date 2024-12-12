import random

class HashTable:
    def __init__(self, size, prime1):
        self.size = size
        self.table = [None] * self.size
        self.prime1 = prime1

    def _hash_multiplicative(self, key):
        """Función multiplicativa para hashing doble, basado en el método de Horner."""
        hash_value = 0
        for byte in range(4):  # Assuming 4-byte keys
            hash_value = (hash_value * self.prime1 + (key & 0xFF)) % self.size
            key >>= 8
        return hash_value

    def insert(self, key):
        hash_value = self._hash_multiplicative(key)
        i = 0
        while self.table[hash_value] is not None:
            hash_value = (hash_value + 1) % self.size
        self.table[hash_value] = key

    def display_insertion_table(self, keys):
        print(f"{'Key':<10}{'Initial Hash':<12}{'Step':<6}{'Table Value'}")
        print('-' * 36)
        for key in keys:
            hash_value = self._hash_multiplicative(key)
            step = 0
            display_row = [f"{key:<10}", f"{hash_value:<12}", "", f"{self.table[hash_value]}"]
            while self.table[hash_value] is not None:
                hash_value = (hash_value + 1) % self.size
                step += 1
                display_row[2] = step
                display_row[3] = self.table[hash_value] if self.table[hash_value] is not None else ""
            print(f"{' '.join(map(str, display_row))}")

# Generar 20 enteros aleatorios en el rango [0, 99999]
random_keys = random.sample(range(100000), 20)

# Prime number for multiplicative hashing
prime1 = 31

# Tabla hash con tamaño 103 y el primo 31 para multiplicar
hash_table = HashTable(103, prime1)

# Insertar y mostrar la tabla de inserción
hash_table.display_insertion_table(random_keys)
