from django.test import TestCase
import unittest
from personas.models import Cliente, Empleado, Producto


# assertTrue
# assertFalse
# assert
class testAlumno(unittest.TestCase):

    def test_crear_cliente(self):
        cliente = Cliente.objects.create(fecha_nacimiento='2000-10-11',
                                         rut='203333-4',
                                         nombre='Benja',
                                         apellido_paterno='Mor',
                                         apellido_materno='Silva',
                                         email='ejemplo123@gmail.com',
                                         genero='masculino',
                                         contrasenia='1234',
                                         foto='',
                                         activo=1)

        cliente.save()

        self.assertTrue(cliente, True)

    def test_crear_empleado(self):
        empleado = Empleado.objects.create(fecha_nacimiento='1998-12-11',
                                           rut='1844446-4',
                                           nombre='Florinda',
                                           apellido_paterno='Valenzuela',
                                           apellido_materno='Vivaldi',
                                           email='ejemplo667@gmail.com',
                                           genero='femenino',
                                           contrasenia='1234',
                                           foto='',
                                           activo=1)

        empleado.save()

        self.assertTrue(empleado, True)

    def test_crear_producto(self):
        producto = Producto.objects.create(
                                           cod_producto='23',
                                           nombre_producto='producto_ejemplo',
                                           precio_producto=10000,
                                           tipo_producto='ejemplo',
                                           foto_producto='',
                                           activo=1)

        producto.save()

        self.assertTrue(producto, True)


# Create your tests here.
