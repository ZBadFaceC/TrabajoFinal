from django import forms


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
