import math

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        """Inserts an item into the heap."""
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Heapifies up to restore the heap property."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Heapifies down to restore the heap property."""
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def levels_loop(self):
        """Returns the number of levels in the heap using a loop."""
        if not self.heap:
            return 0

        levels = 0
        index = 0
        while index < len(self.heap):
            index = (index * 2) + 1
            levels += 1
        return levels

    def levels(self):
        """Returns the number of levels in the heap using logarithm."""
        if not self.heap:
            return 0
        return math.floor(math.log2(len(self.heap)) + 1)

    def display(self):
        """Displays the heap."""
        print(self.heap)

# Ejemplo de uso
heap = Heap()

# Insertar elementos en el heap
for i in range(1, 34):
    heap.insert(i)

# Mostrar la matriz actual
print("Heap actual:")
heap.display()

# Niveles usando bucle
levels_loop = heap.levels_loop()
print(f"\nNúmero de niveles usando levels_loop(): {levels_loop}")

# Niveles usando matemáticas
levels_math = heap.levels()
print(f"Número de niveles usando levels(): {levels_math}")
