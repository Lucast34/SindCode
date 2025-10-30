from django.db import models

# Create your models here.
# Estudar o que é orm (object relation mapper)

#Herença é uma classe herda de outra classe e implementa suas próprias caracteristicas
#Filho(Pai) utilizo o sinal de () para herença

class Categoria(models.Model):# a classe é um conjunto de objetos

    # toda classe começa com letra Maiscula(PascalCase)
    nome= models.CharField(max_length=88, null=False, blank=False)

    #max_length: limitr de caracteres
    #null-> nenhuma informação
    #blank:string vazia""

    def __str__(self):
        return f"Categoria [nome={self.nome}]"