class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def matrix_to_tree(matrix):
    n = len(matrix)
    if not matrix[0]:
        raise ValueError("Root node is missing")

    # Create nodes
    nodes = [[None for _ in row] for row in matrix]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] is not None:
                nodes[i][j] = Node(matrix[i][j])

    # Connect nodes
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if nodes[i][j]:
                left_child_index = 2 * i + 1
                right_child_index = 2 * i + 2
                if left_child_index < n and nodes[left_child_index][j]:
                    nodes[i][j].left = nodes[left_child_index][j]
                if right_child_index < n and nodes[right_child_index][j]:
                    nodes[i][j].right = nodes[right_child_index][j]

    return nodes[0][0]

# Ejemplo de uso
matrix = [[None, None, None],
          [55, 12, 71],
          [55, 12, None, 4],
          [55, 12, None, 4, None, None, None, None, 8, None, None, None, None, None, None, None, None, 6, None],
          [55, 12, None, None, None, None, 4, None, 8, None, None, None, None, None, None, None, None, 6, None]]

try:
    root = matrix_to_tree(matrix)
    # Imprimir el árbol (por ejemplo, usando un recorrido en preorden)
except ValueError as e:
    print(e)