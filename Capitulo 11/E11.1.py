import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def _linear_probe(self, hash_value, i):
        return (hash_value + i) % self.size

    def _quadratic_probe(self, hash_value, i):
        return (hash_value + i**2) % self.size

    def _double_hash(self, hash_value, i):
        return (hash_value + i * (1 + (key % (self.size - 1)))) % self.size

    def insert(self, key, scheme):
        i = 0
        hash_value = self._hash(key)

        while self.table[scheme(hash_value, i)] is not None:
            i += 1

        self.table[scheme(hash_value, i)] = key

    def findClavesDesplazadas(self, scheme):
        displaced_keys_count = 0

        for key in range(200):  # Consider a range of 200 random keys
            hash_value = self._hash(key)
            i = 0

            while self.table[scheme(hash_value, i)] is not None:
                i += 1

            if i > 0:
                displaced_keys_count += 1

        return displaced_keys_count

# Generar claves aleatorias
random_keys = random.sample(range(1000), 200)

# Probar con factores de carga de 0.5, 0.7 y 0.9 para cada esquema
factors = [0.5, 0.7, 0.9]
schemes = ['linear_probe', 'quadratic_probe', 'double_hash']

results = {}

for factor in factors:
    for scheme_name in schemes:
        table = HashTable(int(103 / factor))  # Ajustar el tamaño según el factor de carga
        # Seleccionar función de sonda adecuada
        scheme = getattr(HashTable, scheme_name)

        for key in random_keys:
            table.insert(key, scheme)

        displaced_count = table.findClavesDesplazadas(scheme)
        results[factor, scheme_name] = displaced_count

# Mostrar resultados
for (factor, scheme), displaced_count in results.items():
    print(f"Factor de carga {factor}, Sonda '{scheme}': {displaced_count} claves desplazadas.")
