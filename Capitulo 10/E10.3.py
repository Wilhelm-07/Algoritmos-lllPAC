class Multiset:
    def __init__(self):
        self.tree = AVLTree()

    def __len__(self):
        return len(self.tree)

    def cardinality(self):
        return sum(count for _, count in self.tree)

    def __str__(self):
        return str(list(self.tree))

    def __contains__(self, key):
        return self.tree.find(key) is not None

    def count(self, key):
        node = self.tree.find(key)
        return node.value if node else 0

    def add(self, key, count=1):
        node = self.tree.find(key)
        if node:
            node.value += count
        else:
            self.tree.insert(key, count)

    def remove(self, key, count=1):
        node = self.tree.find(key)
        if node:
            node.value -= count
            if node.value <= 0:
                self.tree.delete(key)

    def union(self, other):
        result = Multiset()
        for key, count in self:
            result.add(key, count)
        for key, count in other:
            result.add(key, max(count, result.count(key)))
        return result

    def intersection(self, other):
        result = Multiset()
        for key, count in self:
            if key in other:
                result.add(key, min(count, other.count(key)))
        return result

    def __iter__(self):
        return self.tree.inorder_traversal()