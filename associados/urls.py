from django.urls import path
from associados.views import associados,login,cadastro

urlpatterns = [
    path('associados', associados ,name='associados'),
    path('cadastro', cadastro ,name='cadastro'),
    path('login', login ,name='login')
]