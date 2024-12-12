class Tree234:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node234(key, data)
        else:
            self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if node.isFull():
            # Node is full, need to split it first
            new_node, middle_key = node.split()
            
            # If the parent is None, the node itself becomes the new root
            if node == self.root:
                new_root = Node234(middle_key)
                new_root.children = [node, new_node]
                self.root = new_root
                return self.__insert(self.root, key, data)
            else:
                # Propagate the split upwards
                self.__insert(self.__find_parent(self.root, node), middle_key, new_node)

        if key < node.keys[0]:
            # Insert in the left child
            self.__insert(node.children[0], key, data)
        elif len(node.keys) == 1 or key < node.keys[1]:
            # Insert in the middle child
            self.__insert(node.children[1], key, data)
        else:
            # Insert in the right child
            self.__insert(node.children[2], key, data)

    def __find_parent(self, current_node, target_node):
        """Recursivamente busca el nodo padre del nodo objetivo."""
        for child in current_node.children:
            if child == target_node:
                return current_node
            else:
                parent = self.__find_parent(child, target_node)
                if parent:
                    return parent
        return None

    def niveles(self, node=None):
        """Devuelve el número de niveles en el árbol. Un árbol vacío tiene 0 niveles."""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        else:
            return node.getHeight()

    def nodos(self, node=None):
        """Devuelve el número de nodos en el árbol. Un árbol vacío tiene 0 nodos."""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return len(list(node.traverse()))

    def items(self, node=None):
        """Devuelve el número de elementos en el árbol. Un árbol vacío tiene 0 elementos."""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return sum(len(n.keys) for n in node.traverse())

    def minItem(self, node=None):
        """Devuelve la clave y los datos del artículo con el mínimo valor en el árbol. 
        Llamar a esto en un árbol vacío debería generar una excepción."""
        if node is None:
            node = self.root
        
        if node is None:
            raise ValueError("El árbol está vacío.")
        
        current = node
        while current.hasChildren():
            current = current.getChild(0)
        return current.keys[0], current.data[0]

    def maxItem(self, node=None):
        """Devuelve la clave y los datos del artículo con el máximo valor en el árbol.
        Llamar a esto en un árbol vacío debería generar una excepción."""
        if node is None:
            node = self.root
        
        if node is None:
            raise ValueError("El árbol está vacío.")
        
        current = node
        while current.hasChildren():
            current = current.getChild(len(current.keys) - 1)
        return current.keys[-1], current.data[-1]

class Node234:
    def __init__(self, key=None, data=None):
        self.keys = [key] if key else []
        self.data = [data] if data else []
        self.children = [None, None, None]

    def isFull(self):
        """Determina si el nodo está lleno (tiene 3 claves)."""
        return len(self.keys) == 3

    def split(self):
        """Divide el nodo lleno y retorna un nuevo nodo y la clave medianera."""
        middle_index = len(self.keys) // 2
        median_key = self.keys[middle_index]
        
        # Crear un nuevo nodo y mover la mitad de las claves y datos a él
        new_node = Node234(self.keys[middle_index+1:], self.data[middle_index+1:])
        
        # Mantener las claves y datos en el nodo original a la izquierda
        self.keys = self.keys[:middle_index]
        self.data = self.data[:middle_index]
        self.children = self.children[:middle_index+1]
        
        return new_node, median_key

    def getHeight(self):
        """Calcula la altura del nodo en el árbol."""
        if not self.hasChildren():
            return 1
        else:
            return 1 + max(child.getHeight() for child in self.children if child)

    def hasChildren(self):
        """Determina si el nodo tiene hijos."""
        return any(self.children)

    def getChild(self, index):
        """Devuelve el hijo en el índice dado."""
        return self.children[index]

    def traverse(self):
        """Recorre el nodo y sus hijos en preorden."""
        yield self
        for child in self.children:
            if child:
                yield from child.traverse()
