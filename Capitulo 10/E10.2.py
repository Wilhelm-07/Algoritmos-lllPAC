class AVLTree:
    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = self.Node(key, data)
        else:
            self.root = self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if node is None:
            return self.Node(key, data)

        if key < node.key:
            node.left = self.__insert(node.left, key, data)
        elif key > node.key:
            node.right = self.__insert(node.right, key, data)
        else:
            # Duplicado, no se permite
            return node

        node.height = 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))
        return self.__balance(node)

    def __balance(self, node):
        balance = self.__getBalance(node)

        if balance > 1:
            if self.__getBalance(node.left) < 0:
                node.left = self.__rotateLeft(node.left)
            return self.__rotateRight(node)

        if balance < -1:
            if self.__getBalance(node.right) > 0:
                node.right = self.__rotateRight(node.right)
            return self.__rotateLeft(node)

        return node

    def __rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.__getHeight(z.left), self.__getHeight(z.right))
        y.height = 1 + max(self.__getHeight(y.left), self.__getHeight(y.right))

        return y

    def __rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.__getHeight(z.left), self.__getHeight(z.right))
        y.height = 1 + max(self.__getHeight(y.left), self.__getHeight(y.right))

        return y

    def __getHeight(self, node):
        if not node:
            return 0
        return node.height

    def __getBalance(self, node):
        if not node:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    def howManyWithin(self, low, high, node=None):
        """Cuenta el número de elementos con claves dentro del rango especificado."""
        if node is None:
            node = self.root

        if node is None:
            return 0

        count = 0

        # Si la clave actual está fuera del rango, descarta esa rama
        if low <= node.key <= high:
            count += 1

        if low < node.key:
            count += self.howManyWithin(low, high, node.left)

        if node.key < high:
            count += self.howManyWithin(low, high, node.right)

        return count

# Ejemplo de uso
avl_tree = AVLTree()
for key in [10, 20, 30, 40, 50, 25, 5]:
    avl_tree.insert(key, str(key))

# Contar elementos dentro de diferentes rangos
print(avl_tree.howManyWithin(15, 35))  # Debería contar 3 elementos: 20, 25, 30
print(avl_tree.howManyWithin(5, 50))   # Debería contar 7 elementos: 10, 20, 30, 40, 50, 25, 5
print(avl_tree.howManyWithin(20, 20))  # Debería contar 1 elemento: 20
print(avl_tree.howManyWithin(50, 100)) # Debería contar 1 elemento: 50
print(avl_tree.howManyWithin(100, 200)) # Debería contar 0 elementos
