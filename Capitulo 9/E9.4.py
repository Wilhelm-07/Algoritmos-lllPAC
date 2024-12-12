class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.items = []  # List to store keys
        self.children = []  # List to store child nodes (if not leaf)

class Tree23:
    def __init__(self):
        self.root = None

    def __insert(self, node, key, value):
        # Base case: Empty tree
        if node is None:
            return key, value, None

        # Leaf node: Find insertion position and insert
        if node.is_leaf:
            i = self._find_insertion_index(node.items, key)
            node.items.insert(i, key)
            node.children.insert(i + 1, None)  # Maintain children list

            # Check for split if node is full
            if len(node.items) > 2:
                return self._split_leaf(node)
            else:
                return None, None, None

        # Internal node: Find child and perform recursive insertion
        i = self._find_insertion_index(node.items, key)
        child = node.children[i]
        promoted_key, promoted_value, split_node = self.__insert(child, key, value)

        # Handle promotion from child
        if promoted_key:
            new_items = node.items[:i] + [promoted_key] + node.items[i:]
            new_children = node.children[:i] + [split_node] + node.children[i + 1:]
            return self._find_insertion_index(new_items, promoted_key), promoted_value, None

        return None, None, None

    def insert(self, key, value):
        # Insert at root
        promoted_key, promoted_value, split_node = self.__insert(self.root, key, value)

        # Create new root if split occurred at root level
        if promoted_key:
            new_root = Node(False)
            new_root.items = [promoted_key]
            new_root.children = [self.root, split_node]
            self.root = new_root

    def _find_insertion_index(self, items, key):
        for i, item in enumerate(items):
            if key <= item:
                return i
        return len(items)

    def _split_leaf(self, node):
        # Split leaf node into two new leaves
        mid_index = len(node.items) // 2
        mid_key = node.items[mid_index]
        mid_value = node.children[mid_index]  # Assuming same index for values

        left_leaf = Node(True)
        left_leaf.items = node.items[:mid_index]
        left_leaf.children = node.children[:mid_index + 1]

        right_leaf = Node(True)
        right_leaf.items = node.items[mid_index + 1:]
        right_leaf.children = node.children[mid_index + 1:]

        return mid_key, mid_value, right_leaf

    def search(self, key):
        node = self.root
        while node:
            if key in node.items:
                return node.items.index(key)  # Return index of the key
            elif node.is_leaf:
                return None  # Key not found in leaf
            i = self._find_insertion_index(node.items, key)
            node = node.children[i]
        return None  # Key not found in the tree

    def __str__(self):
        def _preorder(node, level):
            if node:
                print(" " * level * 2, node.items)
                for child in node.children:
                    _preorder(child, level + 1)

        _preorder(self.root, 0)
        return ""


# Example usage
tree = Tree23()

# Add 10 items (modify the list for different insertions)
items = [5, 8, 2, 1, 9, 3, 7, 4, 6, 10]
for key, value in enumerate(items):
    tree.insert(key,