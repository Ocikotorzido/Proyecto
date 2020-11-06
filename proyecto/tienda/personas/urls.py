
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio/', views.menu, name="inicio"),
    path('listar/', views.listar, name="listar"),
    path('buscar/', views.buscar, name="buscar"),
    path('buscar/buscar_por_rut', views.buscar_por_rut, name="buscar_por_rut"),
    path('eliminar', views.eliminar, name="eliminar"),
    path('eliminar_por_rut', views.eliminar_por_rut, name="eliminar_por_rut"),
    path('agregar', views.agregar, name="agregar"),
    path('agregar_cliente', views.agregar_cliente, name="agregar_cliente"),
    path('editar', views.editar, name="editar"),
    path('buscar_para_editar', views.buscar_para_editar, name="buscar_para_editar"),
    path('actualizar_cliente', views.actualizar_cliente, name="actualizar_cliente"),
    path('menu', views.menu, name="menu"),
    path('menu_login', views.menu_login, name='menu_login'),
    path('gabinete', views.gabinete, name="gabinete"),
    path('gabinete_log', views.gabinete_log, name="gabinete_log"),
    path('audifonos', views.audifonos, name="audifonos"),
    path('audifonos_log', views.audifonos_log, name="audifonos_log"),
    path('mouses', views.mouses, name="mouses"),
    path('mouses_log', views.mouses_log, name="mouses_log"),
    path('FAQ', views.faq, name="FAQ"),
    path('FAQ_log', views.faq_log, name="FAQ_log"),
    path('filtrar_productos', views.filtrar_productos, name="filtrar_productos"),
    path('listar_productos', views.listar_productos, name="listar_productos"),
    path('agregar_producto', views.agregar_producto, name="agregar_producto"),
    path('agregar_el_producto', views.agregar_el_producto, name="agregar_el_producto"),
    path('actualizar_producto', views.actualizar_producto, name="actualizar_producto"),
    path('actualizar_el_producto', views.actualizar_el_producto, name="actualizar_el_producto"),
    path('buscar_producto', views.buscar_producto, name="buscar_producto"),
    path('buscar_pro', views.buscar_pro, name="buscar_pro"),
    path('ver_producto', views.ver_producto, name="ver_producto"),
    path('ver_el_producto', views.ver_el_producto, name="ver_el_producto"),
    path('eliminar_producto', views.eliminar_producto, name="eliminar_producto"),
    path('eliminar_el_producto', views.eliminar_el_producto, name="eliminar_el_producto"),






]