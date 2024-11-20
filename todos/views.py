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
        # Verifica a conexão com o banco de dados executando uma consulta simples
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()  # Executa o comando e obtém o resultado
            if result:
                return HttpResponse("Conexão com o banco de dados bem-sucedida!")
            else:
                return HttpResponse("Falha na conexão com o banco de dados.")
    except Exception as e:
        return HttpResponse(f"Erro ao tentar conectar: {str(e)}")


