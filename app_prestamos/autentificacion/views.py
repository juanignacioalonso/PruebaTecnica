

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from prestamos import models

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        
        print(f'user {user}')
        if user is not None and  user.is_active:
            login(request, user)
            return redirect('listar_pedidos')
        else:
            # Agregar un mensaje de error para mostrar que el inicio de sesión falló.
            return render(request, 'login.html',{'autenticate':False})
            
    return render(request, 'login.html',{'autenticate':True})




def cerrar_sesion(request):
    logout(request)
    return redirect('solicitar_prestamo')