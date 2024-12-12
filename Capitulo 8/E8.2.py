class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def combine(self, other, operator):
        """Combina dos árboles binarios con un operador como raíz."""
        root = BinaryTree(operator)
        root.left = self
        root.right = other
        return root

    def inorder(self):
        """Recorrido inorden del árbol."""
        if self.left:
            print('(', end='')
            self.left.inorder()
        print(self.value, end='')
        if self.right:
            self.right.inorder()
            print(')', end='')

    def postorder(self):
        """Recorrido postorden del árbol."""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end='')

    def preorder(self):
        """Recorrido preorden del árbol."""
        print(self.value, end='')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
def build_expression_tree(expression):
    """Construye un árbol binario a partir de una expresión en sufijo."""
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or token.isalpha():  # Operandos
            stack.append(BinaryTree(token))
        else:
            # Operador
            if len(stack) < 2:
                raise ValueError("La expresión es inválida.")
            right = stack.pop()
            left = stack.pop()
            stack.append(left.combine(right, token))

    if len(stack) != 1:
        raise ValueError("La expresión es inválida.")
    
    return stack[0]

# Función para mostrar la expresión en diferentes órdenes de recorrido
def test_expression_tree(expression):
    tree = build_expression_tree(expression)
    
    print(f"Expresión: {expression}")
    print("Recorrido preorden:", end=' ')
    tree.preorder()
    print("\nRecorrido inorden:", end=' ')
    tree.inorder()
    print("\nRecorrido postorden:", end=' ')
    tree.postorder()
    print("\n")

# Ejemplos de pruebas
expressions = [
    "91 95 + 15 + 19 + 4 *",
    "B B * A C 4 * * -",
    "42",
    "Un 57 #",  # Este debería producir una excepción
    "+ /"  # Este debería producir una excepción
]

for expr in expressions:
    try:
        test_expression_tree(expr)
    except ValueError as e:
        print(f"Error: {e}")
