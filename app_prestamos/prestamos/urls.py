# prestamos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('resultado/', views.resultado_prestamo, name='resultado_prestamo'),
    path('error_api/', views.error_api, name='error_api'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('editar_pedido/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
