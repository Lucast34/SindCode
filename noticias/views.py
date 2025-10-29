from django.shortcuts import render
from django.http import HttpResponse


# funcao
# se def dentro classe = metodo
# se def fora classe = função

# Create your views here.

def index(request):
    # definindo um mock com dict
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


    return render(request,
    'noticias/index.html',
          {'cards':dados})
