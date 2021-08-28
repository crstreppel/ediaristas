from django.urls import path
from .views import *

urlpatterns =[
    path('servicos/cadastrar', cadastrar_servico, name='cadastrar-servico'),
    path('servicos/listar', listar_servicos, name='listar_servicos'),
]