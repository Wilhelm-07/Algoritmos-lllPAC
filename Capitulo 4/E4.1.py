class Stack:
    def __init__(self, maxSize):
        self.__stack = [None] * maxSize
        self.__top = -1
        self.__maxSize = maxSize

    def isEmpty(self):
        """Verifica si la pila está vacía."""
        return self.__top == -1

    def isFull(self):
        """Verifica si la pila está llena."""
        return self.__top == self.__maxSize - 1

    def push(self, item):
        """Inserta un elemento en la pila."""
        if self.isFull():
            raise Exception("Error: Stack is full. Cannot push item.")
        self.__top += 1
        self.__stack[self.__top] = item

    def pop(self):
        """Elimina el elemento superior de la pila."""
        if self.isEmpty():
            raise Exception("Error: Stack is empty. Cannot pop item.")
        item = self.__stack[self.__top]
        self.__top -= 1
        return item

    def peek(self):
        """Devuelve el elemento superior de la pila sin eliminarlo."""
        if self.isEmpty():
            raise Exception("Error: Stack is empty. Cannot peek item.")
        return self.__stack[self.__top]

    def size(self):
        """Devuelve el número de elementos en la pila."""
        return self.__top + 1



def is_palindrome(s):
    # Crear una pila
    stack = Stack(len(s))

    # Convertir la cadena a minúsculas y eliminar espacios y caracteres no alfabéticos
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    # Poner los caracteres de la cadena en la pila
    for char in cleaned_string:
        stack.push(char)

    # Comparar los caracteres de la pila con los de la cadena original
    for char in cleaned_string:
        if char != stack.pop():
            return False
    return True

# Prueba del programa
test_string = "Un hombre, un plan, un canal, Panamá"
result = is_palindrome(test_string)
print(f"La cadena '{test_string}' es un palíndromo: {result}")



La cadena 'Un hombre, un plan, un canal, Panamá' es un palíndromo: True
