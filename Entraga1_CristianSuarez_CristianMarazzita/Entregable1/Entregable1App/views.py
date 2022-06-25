from django.shortcuts import render

from .models import *


# Create your views here.

def inicio(request):
      
    return render(request, "Entregable1App\index.html",{})