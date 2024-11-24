from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from todos.views import view_inical, carrinho, login, criar, verificar_conexao, cadastro  # Importando explicitamente as views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota da tela inicial
    path('', view_inical, name="home"),
    # Rota da tela de carrinho
    path('carrinho/', carrinho, name="carrinho"),
    # Rota da tela de login
    path('login/', login, name="login"),
    # Rota de criação/cadastro
    path('criar/', cadastro, name="cadastro"),
    # Rota de verificação de conexão
    path('verificar-conexao/', verificar_conexao, name='verificar_conexao'),
]
