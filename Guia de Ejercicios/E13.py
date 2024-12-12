def fusionar_listas(lista1, lista2):
    nueva_lista = ListaEnlazada()
    nodo1 = lista1.head
    nodo2 = lista2.head

    while nodo1 and nodo2:
        if nodo1.data <= nodo2.data:
            nueva_lista.agregar_final(nodo1.data)
            nodo1 = nodo1.next
        else:
            nueva_lista.agregar_final(nodo2.data)
            nodo2 = nodo2.next

    while nodo1:
        nueva_lista.agregar_final(nodo1.data)
        nodo1 = nodo1.next
    while nodo2:
        nueva_lista.agregar_final(nodo2.data)
        nodo2 = nodo2.next

    return nueva_lista