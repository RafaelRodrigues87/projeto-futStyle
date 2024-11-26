from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from todos.views import aplicar_desconto, carrinho, login_view, remover_do_carrinho, ver_produtos, cadastro, cadastrar_produto, listar_produtos, adicionar_ao_carrinho, ver_cliente, deletar_cliente, atualizar_telefone # Importando explicitamente as views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota da tela inicial listandos os produtos do banco
    path('', listar_produtos, name="home"),
    # Rota da tela de carrinho
    path('adicionar_ao_carrinho/<int:codproduto>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', carrinho, name='carrinho'),
    path('remover/<int:codproduto>/', remover_do_carrinho, name='remover_do_carrinho'),
    # Rota da tela de login
    path('login/', login_view, name="login"),
    # Rota de criação/cadastro
    path('criar/', cadastro, name="cadastro"),
    # Rota de para ver todos os produtos do banco
    path('todos_produtos/', ver_produtos, name='ver_produtos'),

    path('todos_clientes/', ver_cliente, name='ver_cliente'),

    #rota para deletar cliente
    path('deletar_cliente/<int:cliente_id>/',deletar_cliente, name='deletar_cliente'),

    #atualizar telefone
    path('atualizar_telefone/<int:cliente_id>/<str:novo_telefone>/', atualizar_telefone, name='atualizar_telefone'),
    
    #rota da tela de acionar produto
    path('produtos/', cadastrar_produto, name="produtos"),

    #rota para aplicar desconto
    path('aplicar_desconto/', aplicar_desconto, name='aplicar_desconto'),

]
