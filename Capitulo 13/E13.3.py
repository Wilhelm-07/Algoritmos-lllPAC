import math

class Heap:
    def __init__(self, key_function=lambda x: x):
        self.heap = []
        self.key_function = key_function

    def insert(self, item):
        """Inserts an item into the heap."""
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Heapifies up to restore the heap property."""
        parent_index = (index - 1) // 2
        if index > 0 and self.key_function(self.heap[index]) > self.key_function(self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Heapifies down to restore the heap property."""
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.key_function(self.heap[left_child]) > self.key_function(self.heap[largest]):
            largest = left_child

        if right_child < len(self.heap) and self.key_function(self.heap[right_child]) > self.key_function(self.heap[largest]):
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def merge(self, other_heap):
        """Merges another heap into this heap."""
        if self.key_function != other_heap.key_function:
            raise ValueError("Heaps must have identical key functions for merging.")

        # Merging the heaps into the current one
        self.heap.extend(other_heap.heap)

        # Heapify the combined heap to maintain the heap property
        self._heapify_up(len(self.heap) - 1)
        self._heapify_down(0)

    def display(self):
        """Displays the heap."""
        print(self.heap)

# Ejemplo de uso
heap1 = Heap()
heap2 = Heap()

# Insert elements into the first heap
for i in range(1, 6):
    heap1.insert(i)

# Insert elements into the second heap
for i in range(6, 11):
    heap2.insert(i)

# Display heaps before merging
print("Heap 1 before merging:")
heap1.display()
print("\nHeap 2 before merging:")
heap2.display()

# Merge heap2 into heap1
heap1.merge(heap2)

# Display the merged heap
print("\nHeap 1 after merging:")
heap1.display()
