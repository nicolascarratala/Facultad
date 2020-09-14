from repositorios import Repositorios


class ProductoService:

    # Devuelve repositorio productoList
    def get_productosList(self):
        return Repositorios.productosList

    # parametros : Object producto
    # return: Key id
    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        id_new = int(lastKey) + 1
        Repositorios.productosList[id_new] = producto.__dict__
        return id_new

    # parametros: key id, Object producto
    def delete_producto(self, id):
        if id not in Repositorios.productosList:
            raise ValueError("El id a elminar no existe")
        del Repositorios.productosList[id]

    # Actualiza producto en repositorio memberList
    # parametros :  key legajo , Object member
    def update_producto(self, legajo, producto):
        if id not in Repositorios.productoList:
            raise ValueError("El legajo no existe")
        Repositorios.productoList.update({legajo: producto.__dict__})

    def insertion_sort_precio(self, lista, tipo_orden):
        lista_ordenada = lista.copy()
        for i in range(1, len(lista_ordenada)):
            actual = lista_ordenada[i]
            j = i
            # Desplazamiento de los elementos
            if tipo_orden == 'ascendente':
                while j > 0 and \
                 lista_ordenada[j-1]["_precio"] > actual["_precio"]:
                    lista_ordenada[j] = lista_ordenada[j-1]
                    j = j-1
            if tipo_orden == 'descendente':
                while j > 0 and \
                 lista_ordenada[j-1]["_precio"] < actual["_precio"]:
                    lista_ordenada[j] = lista_ordenada[j-1]
                    j = j-1
            # insertar el elemento en su lugar
            lista_ordenada[j] = actual
        return lista_ordenada
