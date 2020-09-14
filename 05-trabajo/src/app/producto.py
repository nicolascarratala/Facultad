

class Producto():

    def __init__(self, descripcion=' ', precio=0, tipo=' ',idvendedor=' '):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo

    # ----- Descripción -----
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    # ----- Precio -----
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    # ----- Tipo -----
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value
