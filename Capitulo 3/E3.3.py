class Array:
    # ... (resto de la clase Array)

    def deduplicate(self):
        if self.__nItems <= 1:
            return

        j = 1
        for i in range(1, self.__nItems):
            if self.__a[i] != self.__a[i-1]:
                self.__a[j] = self.__a[i]
                j += 1

        self.__nItems = j


        # Suponiendo que el arreglo ya está ordenado
arr = Array(10)
# ... (llenar el arreglo con datos)
arr.deduplicate()