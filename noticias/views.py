from django.shortcuts import render
from django.http import HttpResponse
from noticias.models import Categoria, Noticia
from  noticias.models import Autor


# funcao
# se def dentro classe = metodo
# se def fora classe = função

# Create your views here.

def categorias(request):
    # definindo um mock com dict

    categorias = Categoria.objects.all()
    return render(request,
    'noticias/index.html',
          {'cards':categorias})

    """
    dados = {

        1: {"titulo": "Mulheres dev",
            "conteudo": "Mulheres programadoras em python",
            "data_publicacao": "29/10/2025"
        },
        2: {"titulo": "Programadores kids",
            "conteudo": "Programadoras em python no dia das crianças",
            "data_publicacao": "12/10/2025"
        }
    }
    """

def noticias(request):
        noticias = Noticia.objects.all()
        return render(request,'noticias/index.html',{'noticias':noticias})


def autores(request):
    autores = Autor.objects.all()
    return  render(request,'noticias/nossos_autores.html',{'autores':autores})


def buscar(request):
    noticias = Noticia.objects.all()

    if 'buscar' in request.GET:

        nome_buscar = request.GET["buscar"]

        if nome_buscar:
            noticias = noticias.filter(conteudo__icontains=nome_buscar)

    return render(request, 'noticias/buscar.html', {'noticias':noticias})

def retornar(request):

    noticias = Noticia.objects.all()

    return render(request, 'noticias/index.html', {'noticias':noticias})