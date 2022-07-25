from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def inicio(request):
      
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
        return render(request, r"Entregable1App\index.html",{"url":url})
      
    
    return render(request, r"Entregable1App\index.html",{})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            try:
                avatar = Avatar.objects.get(usuario=request.user)
                url = avatar.imagen.url
            except:
                url = "/media/avatar/generica.jpg"
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"Entregable1App/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save() 
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"Entregable1App/register.html",{"form":form})

    form = UserCreationForm()

    return render(request,"Entregable1App/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")



def canchas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            canchas = Cancha.objects.filter( Q(tipo__icontains=search) | Q(tamaño__icontains=search) ).values()

            return render(request,"Entregable1App/canchas.html",{"canchas":canchas, "search":True, "busqueda":search})

    canchas = Cancha.objects.all()

    return render(request,"Entregable1App/canchas.html",{"canchas":canchas, "search":False})

def crear_canchas(request):
    
    if request.method == "POST":
        
        formulario = CanchasFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            cancha = Cancha(tipo=info["tipo"],tamaño=info["tamaño"],costo=info["costo"], horario=info["horario"])
            cancha.save()

            return redirect("canchas")

        return render(request,"Entregable1App/formulario_canchas.html",{"form":formulario})

    # get
    formulario = CanchasFormulario()
    return render(request,"Entregable1App/formulario_canchas.html",{"form":formulario})

def eliminar_cancha(request,cancha_id):

    cancha = Cancha.objects.get(id=cancha_id)
    cancha.delete()

    return redirect("canchas")

def editar_cancha(request,cancha_id):

    cancha = Cancha.objects.get(id=cancha_id)

    if request.method == "POST":

        formulario = CanchasFormulario(request.POST)

        if formulario.is_valid():
            
            info_cancha = formulario.cleaned_data
            
            cancha.tipo = info_cancha["tipo"]
            cancha.tamaño = info_cancha["tamaño"]
            cancha.costo = info_cancha["costo"]
            cancha.horario = info_cancha["horario"]
            cancha.save()

            return redirect("canchas")
        
    formulario = CanchasFormulario(initial={"tipo":cancha.tipo, "tamaño":cancha.tamaño, "costo": cancha.costo, "horario":cancha.horario})
    
    return render(request,"Entregable1App/formulario_canchas.html",{"form":formulario})



def clientes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            clientes = Cliente.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"Entregable1App/clientes.html",{"clientes":clientes, "search":True, "busqueda":search})

    clientes = Cliente.objects.all()

    return render(request,"Entregable1App/clientes.html",{"clientes":clientes, "search":False})

def crear_clientes(request):
    
    # post
    if request.method == "POST":
        
        formulario = ClientesFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            cliente = Cliente(nombre=info["nombre"],apellido=info["apellido"],email=info["email"])
            cliente.save()

            return redirect("clientes")

        return render(request,"Entregable1App/formulario_clientes.html",{"form":formulario})

    # get
    formulario = ClientesFormulario()
    return render(request,"Entregable1App/formulario_clientes.html",{"form":formulario})

def eliminar_cliente(request,cliente_id):

    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()

    return redirect("clientes")

def editar_cliente(request,cliente_id):

    cliente = Cliente.objects.get(id=cliente_id)

    if request.method == "POST":

        formulario = ClientesFormulario(request.POST)

        if formulario.is_valid():
                
            info_cliente = formulario.cleaned_data
                
            cliente.nombre = info_cliente["nombre"]
            cliente.apellido = info_cliente["apellido"]
            cliente.email = info_cliente["email"]
            cliente.save()

            return redirect("clientes")
    formulario = ClientesFormulario(initial={"nombre":cliente.nombre, "apellido":cliente.apellido, "email": cliente.email})
        
    return render(request,"Entregable1App/formulario_clientes.html",{"form":formulario})


def deportes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            deportes = Deporte.objects.filter( Q(tipo__icontains=search) | Q(costo__icontains=search) ).values()

            return render(request,"Entregable1App/deportes.html",{"deportes":deportes, "search":True, "busqueda":search})

    deportes = Deporte.objects.all()

    return render(request,"Entregable1App/deportes.html",{"deportes":deportes, "search":False})

def crear_deportes(request):
    
    # post
    if request.method == "POST":
        
        formulario = DeportesFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            deporte = Deporte(tipo=info["tipo"],profesor=info["profesor"],costo=info["costo"])
            deporte.save()

            return redirect("deportes")

        return render(request,"Entregable1App/formulario_deportes.html",{"form":formulario})

    # get
    formulario = DeportesFormulario()
    return render(request,"Entregable1App/formulario_deportes.html",{"form":formulario})

def eliminar_deporte(request,deporte_id):

    deporte = Deporte.objects.get(id=deporte_id)
    deporte.delete()

    return redirect("deportes")

def editar_deporte(request,deporte_id):

    deporte = Deporte.objects.get(id=deporte_id)

    if request.method == "POST":

        formulario = DeportesFormulario(request.POST)

        if formulario.is_valid():
            
            info_deporte = formulario.cleaned_data
            
            deporte.tipo = info_deporte["tipo"]
            deporte.profesor = info_deporte["profesor"]
            deporte.costo = info_deporte["costo"]
            deporte.save()

            return redirect("deportes")
        
    formulario = DeportesFormulario(initial={"tipo":deporte.tipo, "profesor":deporte.profesor, "costo": deporte.costo})
    
    return render(request,"Entregable1App/formulario_Deportes.html",{"form":formulario})