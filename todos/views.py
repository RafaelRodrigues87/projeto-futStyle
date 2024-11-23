from django.shortcuts import render # type: ignore
from django.db import connection
from django.http import HttpResponse


#funcao que define as rotas

#tela inical
def view_inical(request):
    return render(request, 'todos/home.html')

#tela carrinho
def carrinho(request):
    return render(request, 'todos/carrinho.html')

#tela de login
def login(request):
    return render(request, 'todos/login.html')

#tela de criaçao
def criar(request):
    return render(request, 'todos/criar.html')

def logado(request):
    return render()


def verificar_conexao(request):
    try:
        # Testa a conexão com o banco
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")  # Executa um comando básico
        return HttpResponse("Conexão com o banco de dados bem-sucedida!", status=200)
    except Exception as e:
        # Caso haja erro, retorna a mensagem com o código de erro
        return HttpResponse(f"Erro ao conectar ao banco de dados: {str(e)}", status=500)


