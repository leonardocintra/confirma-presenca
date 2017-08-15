"""
    Convidado URLs
    Criado por: Leonardo Nascimento Cintra
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Presença confirmada dos convidados
    url(r'^$', views.convidado_list, name='convidado_list'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.convidado_delete, name='convidado_delete'),	
    url(r'^presenca-confirmada/', views.presenca_confirmada, name='presenca_confirmada'),

    # Lista de Convidados pelos noivos
    url(r'^lista/', views.lista_convidado_list, name='lista_convidado_list'),
]