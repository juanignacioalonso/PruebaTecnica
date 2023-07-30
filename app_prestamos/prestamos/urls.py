# prestamos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('resultado/', views.resultado_prestamo, name='resultado_prestamo'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/<int:pedido_id>/editar/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/<int:pedido_id>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),
   
]
