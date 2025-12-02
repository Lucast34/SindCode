from django.shortcuts import render, redirect
from associados.forms import AssociadoForms, LoginForm
from django.contrib.auth.models import User


def associados(request):
    return render(request, 'associados/index.html')

def login(request):
    form = LoginForm()
    return render(request, 'associados/login.html', {'form': form})

def cadastro(request):
    form = AssociadoForms()
    if request.method == 'POST':
        form = AssociadoForms(request.POST)
        if form['senha_1'].value() != form['senha_2'].value():
            return redirect('cadastro')
        
        nome_completo = form['nome_completo'].value()
        nome_social = form['nome_social'].value()
        genero = form['genero'].value()
        email = form['email'].value()
        senha = form['senha_1'].value()
        
        if User.objects.filter(username=nome_completo).exists():
            return redirect('cadastro')
        
        associado = User.objects.create_user(
            username = nome_completo,
            email = email,
            password=senha
            )
        associado.save()
        
        return redirect('login')
        
    return render(request, 'associados/cadastro.html',{'form': form})