from django.urls import path
from .views import cadastrar_servico

urlpatterns =[
    path('servicos/cadastrar', cadastrar_servico, name='cadastrar-servico'),
]