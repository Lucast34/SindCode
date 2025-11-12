from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from noticias.views import index
from noticias.views import autores
from setup.settings import MEDIA_ROOT

urlpatterns = [
    path('',index),
    path('autor/',autores)
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)