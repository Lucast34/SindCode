from django.shortcuts import render
from django.http import HttpResponse

# funcao
# se def dentro classe = metodo
# se def fora classe = função

# Create your views here.

def index(request ):
    return HttpResponse("<h1>Ola mundo</h1>")