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

    def getMaxNum(self):
        """Returns the highest number in the array, or None if there are no numbers."""
        numbers = [x for x in self.__a[:self.__nItems] if isinstance(x, (int, float))]
        return max(numbers, default=None)

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

# Search for specific items
print("Search for 12 returns:", arr.search(12))
print("Search for 12.34 returns:", arr.search(12.34))

# Delete specific items
print("Deleting 0 returns:", arr.delete(0))
print("Deleting 17 returns:", arr.delete(17))

# Update a specific index
print("Setting item at index 3 to 33")
arr.set(3, 33)

# Display the array after deletions
print("Array after deletions has", len(arr), "items:")
arr.traverse()

# Test the getMaxNum method
print("\nTesting getMaxNum:")
print("Maximum number in the array:", arr.getMaxNum())

# Test with no numbers
arr_no_numbers = Array.Array(maxSize)
arr_no_numbers.insert("hello")
arr_no_numbers.insert("world")
print("Array with no numbers:")
arr_no_numbers.traverse()
print("Maximum number in the array with no numbers:", arr_no_numbers.getMaxNum())

# Test with only zeros
arr_zeros = Array.Array(maxSize)
arr_zeros.insert(0)
arr_zeros.insert(0)
arr_zeros.insert(0)
print("Array with only zeros:")
arr_zeros.traverse()
print("Maximum number in the array with only zeros:", arr_zeros.getMaxNum())


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
Search for 12 returns: None
Search for 12.34 returns: 12.34
Deleting 0 returns: True
Deleting 17 returns: False
Setting item at index 3 to 33
Array after deletions has 9 items:
77
99
foo
33
44
55
12.34
baz
-17

Testing getMaxNum:
Maximum number in the array: 99
Array with no numbers:
hello
world
Maximum number in the array with no numbers: None
Array with only zeros:
0
0
0
Maximum number in the array with only zeros: 0
