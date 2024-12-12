from collections import deque

class TwoLevelPriorityQueue:
    def __init__(self):
        self.priority_queues = {}  # Diccionario para mapear prioridades a colas

    def insert(self, item, priority):
        if priority not in self.priority_queues:
            self.priority_queues[priority] = deque()
        self.priority_queues[priority].append(item)

    def remove(self, priority=None):
        if not self.priority_queues:
            raise ValueError("La cola está vacía")
        if priority is None:
            # Obtener la prioridad máxima (menor número)
            max_priority = min(self.priority_queues.keys())
        else:
            max_priority = priority
        if max_priority in self.priority_queues:
            return self.priority_queues[max_priority].popleft()
        else:
            raise ValueError(f"No hay elementos con prioridad {priority}")

    def __iter__(self):
        for priority_queue in self.priority_queues.values():
            yield from priority_queue

    def priorities(self):
        return self.priority_queues.keys()

    def __len__(self):
        return sum(len(queue) for queue in self.priority_queues.values())

        pq = TwoLevelPriorityQueue()
pq.insert("task1", 2)
pq.insert("task3", 1)
pq.insert("task2", 3)

# Eliminar el elemento con la mayor prioridad (menor número)
print(pq.remove())  # Imprime "task3"

# Eliminar un elemento con prioridad específica
print(pq.remove(2))  # Imprime "task1"

# Iterar sobre todos los elementos
for item in pq:
    print(item)

# Iterar sobre las prioridades
for priority in pq.priorities():
    print(priority)