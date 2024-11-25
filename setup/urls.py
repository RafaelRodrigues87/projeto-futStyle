from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from todos.views import view_inical, carrinho, login, criar, verificar_conexao, cadastro, cadastrar_produto, listar_produtos # Importando explicitamente as views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota da tela inicial listandos os produtos do banco
    path('', listar_produtos, name="home"),
    # Rota da tela de carrinho
    path('carrinho/', carrinho, name="carrinho"),
    # Rota da tela de login
    path('login/', login, name="login"),
    # Rota de criação/cadastro
    path('criar/', cadastro, name="cadastro"),
    # Rota de verificação de conexão
    path('verificar-conexao/', verificar_conexao, name='verificar_conexao'),

    #rota da tela de acionar produto
    path('produtos/', cadastrar_produto, name="produtos")

    #rota para listar produdo do banco

]
