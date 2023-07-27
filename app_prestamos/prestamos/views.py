# views.py
# prestamos/views.py
from django.shortcuts import render, redirect
import requests
from .models import Genero, Usuario, PedidoPrestamo
from django.shortcuts import render, redirect, get_object_or_404




def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoPrestamo, id=pedido_id)
    generos = Genero.objects.all()

    if request.method == 'POST':
        # Procesar el formulario y guardar los cambios del pedido
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        genero_id = request.POST['genero']
        email = request.POST['email']
        monto_solicitado = request.POST['monto_solicitado']

        genero = Genero.objects.get(pk=genero_id)
        usuario, _ = Usuario.objects.get_or_create(
            dni=dni,
            defaults={'nombre': nombre, 'apellido': apellido, 'genero': genero, 'email': email}
        )

        pedido.usuario = usuario
        pedido.monto_solicitado = monto_solicitado
        pedido.save()

        return redirect('ver_pedidos')

    return render(request, 'prestamos/editar_pedido.html', {'pedido': pedido, 'generos': generos})

def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoPrestamo, id=pedido_id)

    if request.method == 'POST':
        # Eliminar el pedido de préstamo
        pedido.delete()
        return redirect('ver_pedidos')

    return render(request, 'prestamos/eliminar_pedido.html', {'pedido': pedido})



def solicitar_prestamo(request):
    if request.method == 'POST':
        # Procesar el formulario y crear el usuario y el pedido de préstamo
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        genero_id = request.POST['genero']
        email = request.POST['email']
        monto_solicitado = request.POST['monto_solicitado']

        genero = Genero.objects.get(pk=genero_id)
        usuario, created = Usuario.objects.get_or_create(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            genero=genero,
            email=email
        )

        pedido = PedidoPrestamo.objects.create(
            usuario=usuario,
            monto_solicitado=monto_solicitado
        )

        
        api_url = f"https://api.moni.com.ar/api/v4/scoring/pre-score/[dni]"
        headers = {"credential": "ZGpzOTAzaWZuc2Zpb25kZnNubm5u"}
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            # Suponemos que la API devuelve el resultado en el campo "aprobado" de la respuesta JSON
            data = response.json()
            aprobado = data.get("aprobado", False)
            pedido.aprobado = aprobado
            pedido.save()

        return render(request, 'prestamos/resultado_prestamo.html', {'pedido': pedido})

    generos = Genero.objects.all()
    return render(request, 'prestamos/formulario_prestamo.html', {'generos': generos})






