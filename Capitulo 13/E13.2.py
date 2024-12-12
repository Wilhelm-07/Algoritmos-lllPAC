class Heap:
    def __init__(self, data=None, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap
        if data:
            for item in data:
                self.insert(item)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)] if self.is_min_heap else self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and (self.heap[left] < self.heap[smallest] if self.is_min_heap else self.heap[left] > self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and (self.heap[right] < self.heap[smallest] if self.is_min_heap else self.heap[right] > self.heap[smallest]):
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.extract_min() if not self.is_min_heap else self.extract_min()