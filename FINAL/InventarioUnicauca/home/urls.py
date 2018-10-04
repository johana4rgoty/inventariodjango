from django.urls import path
from .views import *

urlpatterns = [
   
    path('index/', index_view, name='index'),
    path('quienes_somos/', quienes_somos_view, name='quienes_somos'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view,name='logout'),
    
    path('prestamos/',  prestamos_view, name="prestamos"),
    path('prestamosDispositivos/',  prestamosDispositivos_view, name="prestamosDispositivos"),
    path('prestamosIp/',  prestamosIp_view, name="prestamosIp"),
    path('prestamosSalones/',  prestamosSalones_view, name="prestamosSalones"),

    path('informes/',  informes_view, name="informes"), 
    path('perfil/',  perfil_view, name="perfil"), 

    path('lista_sala/', lista_sala_view, name="lista_sala"),
    path('lista_elemento/', lista_elemento_view, name="lista_elemento"),
    path('lista_ip/', lista_ip_view, name="lista_ip"),
    path('lista_usuario/', lista_usuario_view, name="lista_usuario"),
    path('lista_admin/', lista_admin_view, name="admin"),
    

    path('agregar_sala/', agregar_sala_view, name='agregar_sala'),
    path('agregar_ip/', agregar_ip_view, name='agregar_ip'),
    path('agregar_elemento/', agregar_elemento_view, name='agregar_elemento'),
    path('agregar_estudiante/', agregar_estudiante_view, name='agregar_estudiante'),
    path('agregar_profesores/', agregar_profesor_view, name='agregar_profesores'),
    path('agregar_admin/', agregar_admin_view, name='agregar_usuario'),
    path('agregar_user/', agregar_user_view, name='agregar_user'),

    path('ver_ip/<int:id>/', ver_ip_view, name="ver_ip"),
    path('ver_sala/<int:id>/', ver_sala_view, name="ver_sala"),
    path('ver_elemento/<int:id>/', ver_elemento_view, name="ver_elemento"),
    path('ver_usuario/<int:id>/', ver_usuario_view, name="ver_usuario"),

    path('editar_producto/<int:id>/', editar_producto_view, name="editar_producto"),
    path('editar_sala/<int:id>/', editar_sala_view, name="editar_sala"),
    path('editar_ip/<int:id>/', editar_ip_view, name="editar_ip"),
    path('editar_elemento/<int:id>/', editar_elemento_view, name="editar_elemento"),
    path('editar_perfil/<int:id>/', editar_perfil_view, name="editar_perfil"),
    path('editar_usuario/<int:id>/', editar_usuario_view, name="editar_usuario"),

    path('eliminar_producto/<int:id>/', eliminar_producto_view, name="eliminar_producto"),
    path('eliminar_sala/<int:id>/', eliminar_sala_view, name="eliminar_sala"),
    path('eliminar_ip/<int:id>/', eliminar_ip_view, name="eliminar_ip"),
    path('eliminar_elemento/<int:id>/', eliminar_elemento_view, name="eliminar_elemento"),
     path('eliminar_usuario/<int:id>/', eliminar_usuario_view, name="eliminar_usuario"),

    path('desactivar_producto/<int:id>/', desactivar_producto_view, name="desactivar_producto"),    
    path('desactivar_sala/<int:id>/', desactivar_sala_view, name="desactivar_sala"),
    path('desactivar_ip/<int:id>/', desactivar_ip_view, name="desactivar_ip"),
    path('desactivar_elemento/<int:id>/', desactivar_elemento_view, name="desactivar_elemento"),
    path('desactivar_usuario/<int:id>/', desactivar_usuario_view, name="desactivar_usuario"),

   
    
]
