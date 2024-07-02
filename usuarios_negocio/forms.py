from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'apellido', 'password']


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
            elif not user.is_active:
                raise forms.ValidationError("Esta cuenta está desactivada.")
            elif not user.is_staff:
                raise forms.ValidationError("No tienes permisos de administrador.")

        return super().clean()
