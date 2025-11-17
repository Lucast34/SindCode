from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from noticias.views import index
from noticias.views import autores
from noticias.views import buscar
from setup.settings import MEDIA_ROOT

urlpatterns = [
    path('',index),
    path('autor/',autores),
    path("buscar/",buscar, name="buscar")
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)