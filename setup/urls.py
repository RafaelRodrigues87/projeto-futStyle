from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from todos.views import view_inical, carrinho, login, criar, verificar_conexao# Importando explicitamente as views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota da tela inicial
    path('', view_inical, name="home"),
    #rota da tela de carrinho
    path('carrinho/', carrinho, name="carrinho"),
    #rota da tela de login
    path('login/', login, name="login"),
    #rota de criar
    path('criar/', criar, name="criar"),

     path('verificar-conexao/', verificar_conexao, name='verificar_conexao')
]

