class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, key, find_deepest=True):
        # ... (implementación similar al ABB estándar, pero buscando el nodo más profundo o menos profundo)

    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, val)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key, val)
                    return
                node = node.right
            else:  # Clave duplicada
                if find_deepest:
                    while node.left:
                        node = node.left
                node.left = Node(key, val)
                return

    def delete(self, key):
        # ... (implementación similar al ABB estándar, pero buscando el nodo más profundo para eliminar)