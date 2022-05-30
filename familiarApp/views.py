from django.shortcuts import render
from .models import Familiar
# Create your views here.

def funcion (request):
    familiares = Familiar.objects.all()
    return render (request, "familiar.html", {"funcion" : familiares})