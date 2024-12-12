import heapq
from collections import defaultdict

class FrequencyCounter:
    def __init__(self):
        self.word_count = defaultdict(int)
        self.max_heap = []
        self.min_heap = []

    def read_file(self, filename):
        """Lee el archivo de texto y cuenta las palabras"""
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower().strip(".,!?\"':;()[]{}<>")
                    if word:  # Ignore empty words
                        self.word_count[word] += 1

    def build_heaps(self):
        """Construye max-heap y min-heap de las palabras por su recuento"""
        for word, count in self.word_count.items():
            heapq.heappush(self.max_heap, (-count, word))  # max-heap
            heapq.heappush(self.min_heap, (count, word))   # min-heap

    def top_k_words(self, k):
        """Devuelve las k palabras más y menos frecuentes"""
        top_words = heapq.nlargest(k, self.max_heap)
        bottom_words = heapq.nsmallest(k, self.min_heap)
        return top_words, bottom_words

# Ejemplo de uso
filename = 'textfile.txt'  # Replace with the path to your text file
counter = FrequencyCounter()
counter.read_file(filename)
counter.build_heaps()

# Obtener las 20 palabras más frecuentes y menos frecuentes
top_20, bottom_20 = counter.top_k_words(20)

print("20 palabras más frecuentes:")
for count, word in top_20:
    print(f"{word}: {(-count)} veces")

print("\n20 palabras menos frecuentes:")
for count, word in bottom_20:
    print(f"{word}: {count} veces")
