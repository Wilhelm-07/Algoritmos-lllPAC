import heapq
from collections import Counter, defaultdict

class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # 1. Contar la frecuencia de cada carácter
    frequency = Counter(text)

    # 2. Construir la cola de prioridad
    heap = [HuffmanNode(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # 3. Construir el árbol de Huffman
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, code='', huffman_codes={}):
    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = code
        build_huffman_codes(node.left, code + '0', huffman_codes)
        build_huffman_codes(node.right, code + '1', huffman_codes)
    return huffman_codes

def encode(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def decode(binary_message, root):
    current_node = root
    decoded_message = []

    for bit in binary_message:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_message.append(current_node.char)
            current_node = root

    return ''.join(decoded_message)

# Función principal
def huffman_encoding_decoding(text):
    if not text:
        return "", "", 0, 0

    # Construir el árbol de Huffman
    root = build_huffman_tree(text)

    # Construir la tabla de códigos
    huffman_codes = build_huffman_codes(root)

    # Codificar el mensaje
    encoded_message = encode(text, huffman_codes)

    # Decodificar el mensaje
    decoded_message = decode(encoded_message, root)

    # Calcula la cantidad de bits
    num_bits = len(encoded_message)

    return encoded_message, decoded_message, num_bits, len(text)

# Pruebas
texts = [
    "ABRACADABRA",
    "Huffman coding",
    "Huffman",
    "Python is awesome!"
]

for text in texts:
    encoded_message, decoded_message, num_bits, num_chars = huffman_encoding_decoding(text)
    print(f"Texto original: {text}")
    print(f"Mensaje codificado: {encoded_message}")
    print(f"Mensaje decodificado: {decoded_message}")
    print(f"Número de bits en el mensaje codificado: {num_bits}")
    print(f"Número de caracteres en el mensaje original: {num_chars}")
    print()
