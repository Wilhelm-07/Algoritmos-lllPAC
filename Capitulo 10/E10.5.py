import math

class AVLTree:
    # ... (resto de la implementación del AVLTree)

    def __init__(self):
        # ...
        self.stats = {
            'updates': 0,
            'diffs': 0,
            'rot_left': 0,
            'rot_right': 0
        }

    def update_height(self, node):
        # ... (implementación original)
        self.stats['updates'] += 1

    def height_diff(self, node):
        # ... (implementación original)
        self.stats['diffs'] += 1

    def rotate_left(self, z):
        # ... (implementación original)
        self.stats['rot_left'] += 1

    def rotate_right(self, z):
        # ... (implementación original)
        self.stats['rot_right'] += 1

    def get_stats(self):
        return self.stats

    def reset_stats(self):
        self.stats = {
            'updates': 0,
            'diffs': 0,
            'rot_left': 0,
            'rot_right': 0
        }

    def __len__(self):
        # ... (implementación para contar nodos)

    def height(self):
        # ... (implementación para obtener la altura)

def print_stats(tree, n):
    stats = tree.get_stats()
    log_n = math.log(n) if n >= 4 else 1  # Evitar división por cero
    print(f"{'N':>4} {'H':>2} {'updHgt':>6} {'hgtDif':>6} {'RotLft':>6} {'RotRgt':>6} {'updHgt/logN':>10} {'hgtDif/logN':>10} {'RotLft/logN':>10} {'RotRgt/logN':>10}")
    print(f"{n:>4} {tree.height():>2} {stats['updates']:>6} {stats['diffs']:>6} {stats['rot_left']:>6} {stats['rot_right']:>6} {stats['updates']/log_n:>10.3f} {stats['diffs']/log_n:>10.3f} {stats['rot_left']/log_n:>10.3f} {stats['rot_right']/log_n:>10.3f}")
    tree.reset_stats()

# Ejemplo de uso:
tree = AVLTree()
for i in range(100):
    tree.insert(i)
    if i % 10 == 0:
        print_stats(tree, i)