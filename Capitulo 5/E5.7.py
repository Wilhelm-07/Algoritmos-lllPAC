class FibonacciIterator:
    def __init__(self, max_index=100):
        """Inicializa el iterador con un índice máximo."""
        self.max_index = max_index
        self.current_index = 0
        self.fib_sequence = [0, 1]  # Precomputamos los dos primeros números

    def _compute_fib_until(self, index):
        """Computa la secuencia de Fibonacci hasta el índice dado."""
        while len(self.fib_sequence) <= index:
            self.fib_sequence.append(self.fib_sequence[-1] + self.fib_sequence[-2])

    def next(self):
        """Avanza al siguiente número de Fibonacci."""
        if self.current_index >= self.max_index:
            raise StopIteration("No hay más números en la secuencia.")
        if self.current_index >= len(self.fib_sequence):
            self._compute_fib_until(self.current_index)
        value = self.fib_sequence[self.current_index]
        self.current_index += 1
        return value

    def previous(self):
        """Retrocede al número anterior de Fibonacci."""
        if self.current_index <= 0:
            raise StopIteration("No hay más números hacia atrás en la secuencia.")
        self.current_index -= 1
        return self.fib_sequence[self.current_index]

    def current(self):
        """Devuelve el número actual en la secuencia."""
        if self.current_index >= len(self.fib_sequence):
            self._compute_fib_until(self.current_index)
        return self.fib_sequence[self.current_index]

    def reset(self):
        """Reinicia el iterador al inicio de la secuencia."""
        self.current_index = 0


# Crear el iterador con un máximo de 10 números de Fibonacci
fib_iter = FibonacciIterator(max_index=10)

# Avanzar en la secuencia
print("Avanzando:")
try:
    while True:
        print(fib_iter.next(), end=" ")
except StopIteration:
    print("\nFin de la secuencia.")

# Retroceder en la secuencia
print("\nRetrocediendo:")
try:
    while True:
        print(fib_iter.previous(), end=" ")
except StopIteration:
    print("\nInicio de la secuencia.")
