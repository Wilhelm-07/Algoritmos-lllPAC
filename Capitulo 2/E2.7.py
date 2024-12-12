class OrderedRecordArray:
    # ... (código existente de la clase)

    def __init__(self, maxSize):
        self.__a = [None] * maxSize
        self.__nItems = 0
        self.__maxSize = maxSize

    def _expand(self):
        # Expandir la lista en un factor de 2
        new_size = self.__maxSize * 2
        new_a = [None] * new_size
        for i in range(self.__nItems):
            new_a[i] = self.__a[i]
        self.__a = new_a
        self.__maxSize = new_size

    def insert(self, item):
        # ... (código existente del método insert)
        if self.__nItems == self.__maxSize:
            self._expand()
        # Resto del código de inserción