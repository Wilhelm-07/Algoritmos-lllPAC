from Array import Array

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    # Find the index of the maximum element in unsorted array
    max_index = i
    for j in range(i+1, n):
      if arr.get(j) > arr.get(max_index):
        max_index = j

    # Swap the found maximum element with the first element
    arr.set(i, arr.get(max_index))
    arr.set(max_index, arr.get(i))

# ... (resto del código de ArrayClient.py)

# Ejemplo de uso:
arr = Array(10)
# ... (llenar la matriz con números)
selection_sort(arr)
arr.traverse()