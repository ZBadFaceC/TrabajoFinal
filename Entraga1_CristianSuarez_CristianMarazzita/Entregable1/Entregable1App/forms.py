from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CanchasFormulario(forms.Form):
    
    tipo= forms.CharField(max_length=20)
    tamaño = forms.IntegerField()
    costo = forms.FloatField()
    horario = forms.TimeField()

class ClientesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class DeportesFormulario(forms.Form):
    
    tipo = forms.CharField(max_length=30)
    profesor = forms.CharField(max_length=30)
    costo = forms.FloatField()

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}