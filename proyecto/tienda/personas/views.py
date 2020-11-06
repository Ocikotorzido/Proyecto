from django.core.mail import message
from django.shortcuts import render
from .models import Cliente, Producto
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def inicio(request):
    context = {}
    return render(request, 'personas/menu.html', context)


def listar(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'personas/mostrar_datos.html', context)


def buscar(request):
    context = {}
    return render(request, 'personas/boton_buscar.html', context)


def buscar_por_rut(request):
    mi_rut = request.POST['rut']
    cliente = Cliente.objects.get(rut=mi_rut)
    context = {'cliente': cliente}
    return render(request, 'personas/datos_cliente.html', context)


def eliminar(request):
    context = {}
    return render(request, 'personas/eliminar.html', context)


def eliminar_por_rut(request):
    mi_rut = request.POST['rut']
    cliente = Cliente.objects.get(rut=mi_rut)
    cliente.delete()
    context = {}
    return render(request, 'personas/mensaje_eliminar.html', context)


def agregar(request):
    context = {}
    return render(request, 'personas/formulario_agregar.html', context)


def agregar_cliente(request):
    if request.method == 'POST':
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_paterno = request.POST['apaterno']
        mi_materno = request.POST['amaterno']
        mi_email = request.POST['email']
        mi_fechaNac = request.POST['fecha_nacimiento']
        mi_contrasenia = request.POST['contrasenia']
        mi_genero = request.POST['genero']
        mi_foto = request.FILES['foto']
        if mi_rut != "":
            try:
                cliente = Cliente()

                cliente.rut = mi_rut
                cliente.nombre = mi_nombre
                cliente.apellido_paterno = mi_paterno
                cliente.apellido_materno = mi_materno
                cliente.email = mi_email
                cliente.fecha_nacimiento = mi_fechaNac
                cliente.contrasenia = mi_contrasenia
                cliente.genero = mi_genero
                cliente.activo = 1
                cliente.foto = mi_foto
                cliente.save()

                return render(request, 'personas/mensaje_datos_grabados.html', {})

            except cliente.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def editar(request):
    context = {}
    return render(request, 'personas/editar.html', context)


def buscar_para_editar(request):
    mi_rut = request.POST['rut']
    cliente = Cliente.objects.get(rut=mi_rut)
    context = {'cliente': cliente}
    return render(request, 'personas/formulario_editar.html', context)


def actualizar_cliente(request):
    if request.method == 'POST':
        mi_id = request.POST['id_cliente']
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_paterno = request.POST['aPaterno']
        mi_materno = request.POST['aMaterno']
        mi_fechaNac = request.POST['fechaNac']
        mi_genero = request.POST['genero']

        if mi_rut != "":
            try:
                cliente = Cliente()

                cliente.id_cliente = mi_id
                cliente.rut = mi_rut
                cliente.nombre = mi_nombre
                cliente.apellido_paterno = mi_paterno
                cliente.apellido_materno = mi_materno
                cliente.fecha_nacimiento = mi_fechaNac
                cliente.genero = mi_genero
                cliente.activo = 1

                cliente.save()

                return render(request, 'personas/mensaje_datos_grabados.html', {})

            except cliente.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def menu(request):
    productos = Producto.objects.all()
    context = {'productos': productos}

    return render(request, 'personas/menu_cliente.html', context)


def gabinete(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="gabinete")
    context = {'productos': productos}
    return render(request, 'personas/gabinete.html', context)


def gabinete_log(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="gabinete")
    context = {'productos': productos}
    return render(request, 'personas/user_log/gabinete_log.html', context)


def audifonos(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="audifono")
    context = {'productos': productos}
    return render(request, 'personas/audifonos.html', context)


def audifonos_log(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="audifono")
    context = {'productos': productos}
    return render(request, 'personas/user_log/audifonos_log.html', context)


def mouses(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="mouse")
    context = {'productos': productos}
    return render(request, 'personas/mouses.html', context)


def mouses_log(request):
    productos = Producto.objects.filter(activo=1, tipo_producto="mouse")
    context = {'productos': productos}
    return render(request, 'personas/user_log/mouses_log.html', context)


def faq(request):
    context = {}
    return render(request, 'personas/FAQ.html', context)


def faq_log(request):
    context = {}
    return render(request, 'personas/user_log/FAQ_log.html', context)


def menu_login(request):
    productos = Producto.objects.all()
    context = {'productos': productos}


    return render(request, 'personas/user_log/menu_login.html', context)


def filtrar_productos(request):
    print("hola estoy en la vista listar")
    # select * from alumno
    productos = Producto.objects.filter(activo=1, tipo_producto="audifono")
    context = {'productos': productos}
    return render(request, 'personas/mostrar_filtrado.html', context)


def listar_productos(request):
    print("hola estoy en la vista listar")
    # select * from alumno
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'personas/listar_productos.html', context)

def agregar_producto(request):
    context = {}
    return render(request, 'personas/formulario_productos.html', context)


def agregar_el_producto(request):

    if request.method == 'POST':
        mi_cod = request.POST['cod_producto']
        mi_nombre = request.POST['nombre_producto']
        mi_precio = request.POST['precio_producto']
        mi_tipo = request.POST['tipo_producto']
        mi_foto = request.FILES['foto_producto']
        if mi_cod != "":
            try:
                producto = Producto()

                producto.cod_producto = mi_cod
                producto.nombre_producto = mi_nombre
                producto.precio_producto = mi_precio
                producto.tipo_producto = mi_tipo

                producto.activo = 1
                producto.foto_producto = mi_foto
                producto.save()

                return render(request, 'personas/mensaje_datos_grabados.html', {})

            except producto.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def actualizar_producto(request):
    context = {}
    return render(request, 'personas/buscar_producto.html', context)

def ver_el_producto(request):
    mi_cod = request.POST['cod_producto']
    producto = Producto.objects.get(cod_producto=mi_cod)
    context = {'producto': producto}
    return render(request, 'personas/actualizar_producto.html', context)







def actualizar_el_producto(request):
    if request.method == 'POST':
        mi_id = request.POST['id_producto']
        mi_cod = request.POST['cod_producto']
        mi_nombre = request.POST['nombre_producto']
        mi_precio = request.POST['precio_producto']
        mi_tipo = request.POST['tipo_producto']

        if mi_cod != "":
            try:
                producto = Producto()
                producto.id_producto = mi_id
                producto.cod_producto = mi_cod
                producto.nombre_producto = mi_nombre
                producto.precio_producto = mi_precio
                producto.tipo_producto = mi_tipo

                producto.activo = 1

                producto.save()

                return render(request, 'personas/mensaje_datos_grabados.html', {})

            except producto.DoesNotExist:
                return render(request, 'personas/error/error_204.html', {})
        else:
            return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def buscar_producto(request):
    context = {}
    return render(request, 'personas/buscar_pro.html', context)




def ver_producto(request):
    mi_cod = request.POST['cod_producto']
    producto = Producto.objects.get(cod_producto=mi_cod)
    context = {'producto': producto}
    return render(request, 'personas/dato_producto.html', context)




def buscar_pro(request):
    mi_cod = request.POST['cod_producto']
    producto = Producto.objects.get(cod_producto=mi_cod)
    context = {'producto': producto}
    return render(request, 'personas/actualizar_producto.html', context)




def eliminar_producto(request):
    context = {}
    return render(request, 'personas/eliminar_producto.html', context)


def eliminar_el_producto(request):
    mi_cod = request.POST['cod_producto']
    producto = Producto.objects.get(cod_producto=mi_cod)
    producto.delete()
    context = {}
    return render(request, 'personas/mensaje_eliminado.html', context)
















