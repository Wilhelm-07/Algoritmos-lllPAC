class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ... (otras funciones del árbol)

    def node_count(self, node):
        if not node:
            return 0
        return 1 + self.node_count(node.left) + self.node_count(node.right)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def node_balance(self, node):
        if not node:
            return 0
        return self.node_count(node.right) - self.node_count(node.left)

    def level_balance(self, node):
        if not node:
            return 0
        return self.height(node.right) - self.height(node.left)

    def unbalanced_nodes(self, node, by=1, unbalanced=[]):
        if not node:
            return
        if abs(self.node_balance(node)) > by or abs(self.level_balance(node)) > by:
            unbalanced.append(node.key)
        self.unbalanced_nodes(node.left, by, unbalanced)
        self.unbalanced_nodes(node.right, by, unbalanced)
        return unbalanced