class SortedArray:
    def __init__(self, key_extractor):
        self.array = []
        self.key_extractor = key_extractor

    def __len__(self):
        return len(self.array)

    def get(self, i):
        return self.array[i]

    def find_index(self, key):
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.key_extractor(self.array[mid]) == key:
                # Find the first occurrence of the key
                while mid > 0 and self.key_extractor(self.array[mid - 1]) == key:
                    mid -= 1
                return mid
            elif self.key_extractor(self.array[mid]) < key:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def search(self, key):
        index = self.find_index(key)
        if index < len(self.array) and self.key_extractor(self.array[index]) == key:
            return self.array[index]
        return None

    def insert(self, record):
        index = self.find_index(self.key_extractor(record))
        self.array.insert(index, record)

    def delete(self, record):
        index = self.find_index(self.key_extractor(record))
        if index < len(self.array) and self.array[index] == record:
            self.array.pop(index)