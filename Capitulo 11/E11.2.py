import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash_fold3(self, key):
        """Método de plegado de dígitos: grupos de tres dígitos."""
        key_str = str(key)
        sum_digits = sum(int(key_str[i:i+3]) for i in range(0, len(key_str), 3))
        return sum_digits % self.size

    def _hash_fold2(self, key):
        """Método de plegado de dígitos: grupos de dos dígitos."""
        key_str = str(key)
        sum_digits = sum(int(key_str[i:i+2]) for i in range(0, len(key_str), 2))
        return sum_digits % self.size

    def _linear_probe(self, hash_value, i):
        return (hash_value + i) % self.size

    def insert(self, key, scheme):
        i = 0
        hash_value = scheme(key)

        while self.table[self._linear_probe(hash_value, i)] is not None:
            i += 1

        self.table[self._linear_probe(hash_value, i)] = key

    def findClavesDesplazadas(self, scheme):
        displaced_keys_count = 0

        for key in random_keys:
            hash_value = scheme(key)
            i = 0

            while self.table[self._linear_probe(hash_value, i)] is not None:
                i += 1

            if i > 0:
                displaced_keys_count += 1

        return displaced_keys_count

# Generar 1000 enteros aleatorios de 10 dígitos
random_keys = random.sample(range(10000000000), 1000)

# Probar con factores de carga de 0.5, 0.7 y 0.9 para ambas funciones de plegado
factors = [0.5, 0.7, 0.9]
hash_functions = [HashTable._hash_fold3, HashTable._hash_fold2]

results = {}

for factor in factors:
    for func in hash_functions:
        table = HashTable(int(103 / factor))  # Ajustar el tamaño según el factor de carga
        
        for key in random_keys:
            table.insert(key, func)

        displaced_count = table.findClavesDesplazadas(func)
        func_name = func.__name__
        results[factor, func_name] = displaced_count

# Mostrar resultados
for (factor, func_name), displaced_count in results.items():
    print(f"Factor de carga {factor}, Función de plegado '{func_name}': {displaced_count} claves desplazadas.")
