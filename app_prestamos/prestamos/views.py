# views.py
# prestamos/views.py
from django.shortcuts import render, redirect
import requests
from .models import Genero, Usuario, PedidoPrestamo
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login





def listar_pedidos(request):
    print('inicio listar pedido')
    if not request.user.is_active:
        # Redirigir a la página de inicio o mostrar un mensaje de error.
        return render(request,'prestamos/formulario_prestamo.html')  
    print('en el if del listar pedido')
    pedidos = PedidoPrestamo.objects.all()
    print('despues del object listar pedido')
    return render(request, 'prestamos/listar_pedidos.html', {'pedidos': pedidos})

def editar_pedido(request, pedido_id):
    if not request.user.is_active:
        # Redirigir a la página de inicio o mostrar un mensaje de error.
        return render(request,'prestamos/formulario_prestamo.html')

    pedido = get_object_or_404(PedidoPrestamo, pk=pedido_id)
    if request.method == 'POST':
        # Procesar el formulario de edición aquí y guardar los cambios.
        
        return redirect('listar_pedidos')

    return render(request, 'prestamos/editar_pedido.html', {'pedido': pedido})

def eliminar_pedido(request, pedido_id):
    if not request.user.is_active:
        # Redirigir a la página de inicio o mostrar un mensaje de error.
        return render(request,'prestamos/formulario_prestamo.html')  

    pedido = get_object_or_404(PedidoPrestamo, pk=pedido_id)
    if request.method == 'POST':
        # Eliminar el pedido aquí.
        pedido.delete()
        return redirect('listar_pedidos')

    return render(request, 'prestamos/eliminar_pedido.html', {'pedido': pedido})



def solicitar_prestamo(request):
    
    if request.method == 'GET':
        generos=Genero.objects.all()
        return render(request, 'prestamos/formulario_prestamo.html', {'generos': generos})

    if request.method == 'POST':
        print('metodo post genero ')
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        genero = request.POST['genero']
        email = request.POST['email']
        monto_solicitado = request.POST['monto_solicitado']
        print(f'dni: {dni}')
        print(f'nombre: {nombre}')
        print(f'apellido: {apellido}')
        print(f'genero: {genero}')
        print(f'email: {email}')
        print(f'monto_solicitado: {monto_solicitado}')
        
        # Lógica para verificar el préstamo con la API y actualizar el campo "aprobado"
        api_url = f"https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}"

        headers = {'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            
            body = response.text
            print(body)
            data = json.loads(body)

        # Verificar si el valor del campo "status" es "approve"
            if data.get("status") == "approve":
                aprobado = True
            else:
                aprobado = False
        else:
            # Si hay un error en la API, muestra un mensaje de error
            return render(request, 'prestamos/error_api.html')
            #aprobado=False

       
        
        

        # Crear el pedido de préstamo con el usuario y el estado aprobado
        pedido = PedidoPrestamo.objects.create(dni=dni, monto_solicitado=monto_solicitado, aprobado=aprobado)

        return render(request,'prestamos/resultado_prestamo.html', {'pedido':pedido})

    return render(request, 'prestamos/formulario_prestamo.html')


def resultado_prestamo(request, pedido_id):
    try:
        pedido = PedidoPrestamo.objects.get(pk=pedido_id)
    except PedidoPrestamo.DoesNotExist:
        # Si no se encuentra el pedido, redirige a una página de error o muestra un mensaje
        return render(request, 'prestamos/error_pedido.html')

    return render(request, 'prestamos/resultado_prestamo.html', {'pedido': pedido})







