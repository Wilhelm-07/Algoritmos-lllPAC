from collections import deque

def reorganize_queue(queue):
    even = deque()
    odd = deque()
    
    while queue:
        num = queue.popleft()
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return even + odd

# Prueba del programa
queue = deque([1, 2, 3, 4, 5, 6])
print("Cola original:", list(queue))
reorganized = reorganize_queue(queue)
print("Cola reorganizada:", list(reorganized))
