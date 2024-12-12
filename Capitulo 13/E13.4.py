class Heap:
    # ... (existing implementation)

    def replaceItem(self, old_item, new_item):
        if old_item not in self.heap:
            raise ValueError("Item not found in the heap")

        index = self.heap.index(old_item)
        self.heap[index] = new_item

        if self.is_min_heap:
            if new_item < old_item:
                self.heapify_up(index)
            else:
                self.heapify_down(index)
        else:
            if new_item > old_item:
                self.heapify_up(index)
            else:
                self.heapify_down(index)