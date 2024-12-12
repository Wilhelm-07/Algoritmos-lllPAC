from itertools import permutations

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotateLeft(self, z):
        # ... (implementación estándar de rotación izquierda)

    def rotateRight(self, z):
        # ... (implementación estándar de rotación derecha)

    def insert(self, key):
        # ... (implementación estándar de inserción en AVL, actualizando alturas y realizando rotaciones si es necesario)

    def delete(self, key):
        # ... (implementación estándar de eliminación en AVL)

    def isBalanced(self, node=None):
        if not node:
            node = self.root
        if not node:
            return True
        if abs(self.balance(node)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)

def experiment(keys):
    balanced_count = 0
    for perm in permutations(keys):
        tree = AVLTree()
        for key in perm:
            tree.insert(key)
        if tree.isBalanced():
            balanced_count += 1
    return balanced_count / len(list(permutations(keys)))

# Ejemplo de uso
keys = [1, 2, 3, 4, 5, 6]
probability = experiment(keys)
print("Probabilidad de obtener un árbol AVL equilibrado:", probability)