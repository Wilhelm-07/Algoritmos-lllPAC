class Tree234:
    def __init__(self):
        self.root = None

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
        
        # Usando traverse() para recorrer todos los nodos
        return len(list(node.traverse()))

    def items(self, node=None):
        """Devuelve el número de elementos en el árbol. Un árbol vacío tiene 0 elementos."""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        # Usando traverse() para contar todos los elementos
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
