from django.db import models


# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='id_cliente', primary_key=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=40, blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    contrasenia = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "rut: " + (str(self.rut)) + ", " + (str(self.nombre)) + ", " + (
            str(self.apellido_paterno)) + ", " + (str(self.apellido_materno)) + ", " + (
            str(self.fecha_nacimiento)) + ", " + (str(self.email)) + ", " + (str(self.genero)) + ", " + (
            str(self.foto)) + ", " + (str( self.activo))


class Empleado(models.Model):
    id_empleados = models.AutoField(db_column='id_empleados', primary_key=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=40, blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    contrasenia = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "rut: " + (str(self.rut)) + ", " + (str(self.nombre)) + ", " + (
            str(self.apellido_paterno)) + ", " + (str(self.apellido_materno)) + ", " + (
            str(self.fecha_nacimiento)) + ", " + (str(self.email)) + ", " + (str(self.genero)) + ", " + (
            str(self.foto)) + ", " + (str( self.activo))


class Producto(models.Model):
    id_producto = models.AutoField(db_column='id_producto', primary_key=True)
    cod_producto = models.IntegerField(null=False, unique=True)
    nombre_producto = models.CharField(max_length=30, blank=True, null=True)
    precio_producto = models.IntegerField(blank=False, null=False)
    tipo_producto = models.CharField(max_length=30, blank=True, null=True)
    foto_producto = models.ImageField(upload_to='fotos', blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "cod: " + (str(self.cod_producto)) + ", " + (str(self.nombre_producto)) + ", " + (
            str(self.precio_producto)) \
               + ", " + (str(self.tipo_producto)) + ", " + (str(self.foto_producto)) + ", " + (str(self.activo))


