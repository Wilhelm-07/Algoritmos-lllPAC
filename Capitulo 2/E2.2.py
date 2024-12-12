class Array:
    def __init__(self, initialSize):
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # Number of items in the array initially

    def __len__(self):
        return self.__nItems  # Return number of items

    def get(self, n):
        if 0 <= n < self.__nItems:  # Check bounds
            return self.__a[n]
        return None

    def set(self, n, value):
        if 0 <= n < self.__nItems:  # Check bounds
            self.__a[n] = value

    def insert(self, item):
        if self.__nItems < len(self.__a):  # Ensure space is available
            self.__a[self.__nItems] = item
            self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        index = self.find(item)
        return self.get(index) if index != -1 else None

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]  # Shift elements left
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def deleteMaxNum(self):
        """Returns and removes the highest number in the array, or None if there are no numbers."""
        max_index = None
        max_value = None

        # Find the highest number and its index
        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int, float)):
                if max_value is None or self.__a[i] > max_value:
                    max_value = self.__a[i]
                    max_index = i

        # If a maximum number was found, remove it
        if max_index is not None:
            for k in range(max_index, self.__nItems - 1):
                self.__a[k] = self.__a[k + 1]  # Shift elements left
            self.__nItems -= 1
            return max_value

        return None  # No numeric values found


import Array

# Create an Array object with a maximum size
maxSize = 10
arr = Array.Array(maxSize)

# Insert various items into the array
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

# Display the array contents
print("Array containing", len(arr), "items:")
arr.traverse()

# Test deleteMaxNum
print("\nTesting deleteMaxNum:")
max_num = arr.deleteMaxNum()
print("Deleted max number:", max_num)
print("Array after deleting max number:")
arr.traverse()

# Test deleteMaxNum multiple times
while (max_num := arr.deleteMaxNum()) is not None:
    print(f"Deleted max number: {max_num}")

print("Array after removing all numeric values:")
arr.traverse()

# Test deleteMaxNum on an array with no numbers
arr_no_numbers = Array.Array(maxSize)
arr_no_numbers.insert("hello")
arr_no_numbers.insert("world")
print("\nArray with no numbers:")
arr_no_numbers.traverse()
print("Deleted max number from array with no numbers:", arr_no_numbers.deleteMaxNum())


Array containing 10 items:
77
99
foo
bar
44
55
12.34
0
baz
-17

Testing deleteMaxNum:
Deleted max number: 99
Array after deleting max number:
77
foo
bar
44
55
12.34
0
baz
-17

Deleted max number: 77
Deleted max number: 55
Deleted max number: 44
Deleted max number: 12.34
Deleted max number: 0
Deleted max number: -17
Array after removing all numeric values:
foo
bar
baz

Array with no numbers:
hello
world
Deleted max number from array with no numbers: None
