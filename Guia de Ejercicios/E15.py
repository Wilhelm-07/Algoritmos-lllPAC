from collections import deque

def sort_queue(queue):
    n = len(queue)
    for i in range(n):
        for j in range(n - 1 - i):
            a = queue.popleft()
            b = queue.popleft()
            if a > b:
                queue.append(b)  # Enqueue el menor primero
                queue.append(a)
            else:
                queue.append(a)  # Enqueue el mayor primero
                queue.append(b)
        # Recolocar el elemento más grande al final
        for _ in range(n - 1 - i):
            queue.append(queue.popleft())
    return queue

# Prueba del programa
queue = deque([4, 3, 2, 1, 5])
print("Cola original:", list(queue))
sorted_queue = sort_queue(queue)
print("Cola ordenada:", list(sorted_queue))
