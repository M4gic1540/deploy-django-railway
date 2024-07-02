from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombre, apellido, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        usuario = self.model(
            username=username,
            email=email,
            nombre=nombre,
            apellido=apellido,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, username, email, nombre, apellido, password=None, **extra_fields):
        return self._create_user(
            username,
            email,
            nombre,
            apellido,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(self, username, email, nombre, apellido, password=None, **extra_fields):
        return self._create_user(
            username,
            email,
            nombre,
            apellido,
            password,
            True,
            True,
            **extra_fields
        )


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electrónico',
                              unique=True, max_length=250)
    nombre = models.CharField('Nombre', max_length=200)
    apellido = models.CharField('Apellidos', max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.username})'

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

    def get_short_name(self):
        return self.nombre


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('initiated', 'Initiated'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    buy_order = models.CharField(max_length=64, unique=True)
    session_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='initiated')
    response_code = models.IntegerField(null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    token_ws = models.CharField(
        max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        return f'Transaction {self.buy_order} - {self.status}'
