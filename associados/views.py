from django.shortcuts import render

# Create your views here.
def associados(request ):
    return render(request,'associados/index.html')
def login(request ):
    return render(request,'associados/login.html')
def cadastro(request ):
    return render(request,'associados/cadastro.html')

