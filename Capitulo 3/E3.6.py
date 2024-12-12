class Array:
    # ... (resto de la clase Array)

    def insertion_sort_and_dedup(self):
        n = self.__nItems
        for i in range(1, n):
            key = self.__a[i]
            j = i - 1
            # Marcar duplicados con un valor especial (e.g., -inf)
            while j >= 0 and self.__a[j] == key:
                j -= 1
            # Si no es un duplicado, realizar la inserción
            if j >= 0 and self.__a[j] != key:
                while j >= 0 and self.__a[j] > key:
                    self.__a[j+1] = self.__a[j]
                    j -= 1
                self.__a[j+1] = key
            # Si es un duplicado, moverlo al inicio
            else:
                while j >= 0:
                    self.__a[j+1] = self.__a[j]
                    j -= 1
                self.__a[0] = key

        # Eliminar los duplicados al final
        i = 0
        while i < n and self.__a[i] == float('-inf'):
            i += 1
        for j in range(i, n):
            self.__a[j-i] = self.__a[j]
        self.__nItems = n - i