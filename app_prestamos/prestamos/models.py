from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class PedidoPrestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobado = models.BooleanField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo de {self.usuario}: {self.monto_solicitado}"
