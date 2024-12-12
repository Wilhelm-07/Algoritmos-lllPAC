class Multiset:
    # ... (previous implementation)

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