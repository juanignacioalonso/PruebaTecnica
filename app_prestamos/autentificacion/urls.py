
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
