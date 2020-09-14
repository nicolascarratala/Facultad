import unittest
import render.main
from render.BrowserEngine import Editar
from app.producto import Producto
from parameterized import parameterized
from app.productoServices import ProductoService
from app.repositorios import Repositorios



class TestProducto(unittest.TestCase):

    def test_uso_property(self):

        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        result = self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras'})
        if result is None:
            Editar().add_data("test_uso_property", "OK")
        if result is not None:   
            Editar().add_data("test_uso_property", "No") 

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        result = self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras'})

        if result is None:
            Editar().add_data("test_constructor_con_valores_iniciales", "OK")
        if result is not None:   
            Editar().add_data("test_constructor_con_valores_iniciales", "No") 

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)
    """
    # Eliminar un producto
    def test_delete_producto(self):
        ProductoService().delete_producto(0)
        self.assertEqual(Repositorios.productosList.get(0), None)
        print(ProductoService().get_productosList())

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1) """


if __name__ == '__main__':
    unittest.main()
    