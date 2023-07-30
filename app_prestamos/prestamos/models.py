from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

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
    dni = models.CharField(max_length=10, default='')
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobado = models.BooleanField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo de {self.usuario}: {self.monto_solicitado}"
    


class MiUsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe estar configurado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class MiUsuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    @staticmethod
    def hash_password(password):
        # Utiliza make_password para encriptar la contraseña
        return make_password(password)

    objects = MiUsuarioManager()

    USERNAME_FIELD = 'email'    
