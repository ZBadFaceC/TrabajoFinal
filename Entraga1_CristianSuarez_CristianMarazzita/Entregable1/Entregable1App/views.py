from django.shortcuts import redirect, render
from .models import *
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def inicio(request):
      
    return render(request, r"Entregable1App\index.html",{})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"ProyectoCoderApp/login.html",{"form":form})

def canchas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            canchas = Cancha.objects.filter( Q(tipo__icontains=search) | Q(tamaño__icontains=search) ).values()

            return render(request,"Entregable1App/canchas.html",{"canchas":canchas, "search":True, "busqueda":search})

    canchas = Cancha.objects.all()

    return render(request,"Entregable1App/canchas.html",{"canchas":canchas, "search":False})

def clientes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            clientes = Cliente.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"Entregable1App/clientes.html",{"clientes":clientes, "search":True, "busqueda":search})

    clientes = Cliente.objects.all()

    return render(request,"Entregable1App/clientes.html",{"clientes":clientes, "search":False})

def deportes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            deportes = Deporte.objects.filter( Q(tipo__icontains=search) | Q(costo__icontains=search) ).values()

            return render(request,"Entregable1App/deportes.html",{"deportes":deportes, "search":True, "busqueda":search})

    deportes = Deporte.objects.all()

    return render(request,"Entregable1App/deportes.html",{"deportes":deportes, "search":False})

def crear_canchas(request):
    
    # post
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