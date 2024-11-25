from django.shortcuts import render, redirect # type: ignore
from django.db import connection
from django.http import HttpResponse
# from .forms import ClienteForm, ProdutoForm
from .models import Cliente, Produto

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

def produto(request):
    return render(request, 'todos/produto.html')

def verificar_conexao(request):
    try:
        # Testa a conexão com o banco
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM todos_produto WHERE codproduto = 2;")  # Executa um comando básico
        return HttpResponse("Remocao de dados bem sucecido", status=200)
    except Exception as e:
        # Caso haja erro, retorna a mensagem com o código de erro
        return HttpResponse(f"Erro ao conectar ao banco de dados: {str(e)}", status=500)
    

# cadastrar cliente
def cadastro(request):
    if request.method == 'POST':
        # Captura os dados do formulário via POST
        cliente_nome = request.POST.get('cliente_nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Valida se os campos obrigatórios foram preenchidos
        if cliente_nome and email and endereco and telefone and cpf and data_nascimento and password and password_confirm:
            # Verifica se as senhas coincidem
            if password != password_confirm:
                return HttpResponse("As senhas não correspondem.")

            # Cria um novo cliente e salva no banco de dados
            cliente = Cliente(
                cliente_nome=cliente_nome,
                email=email,
                endereco=endereco,
                telefone=telefone,
                cpf=cpf,
                data_nascimento=data_nascimento,
                password=password
            )
            cliente.save()  # Salva o cliente no banco de dados
            return redirect('home')  # Redireciona para a página inicial após salvar
        else:
            # Se algum campo obrigatório estiver vazio, exibe mensagem de erro
            return HttpResponse("Por favor, preencha todos os campos obrigatórios.")

    # Se a requisição for GET, apenas exibe o formulário vazio
    return render(request, 'todos/criar.html')

#castrar produto

def cadastrar_produto(request):
    if request.method == 'POST':
        produto_nome = request.POST.get('produto_nome')
        preco = request.POST.get('preco')
        produto_quantidade = request.POST.get('produto_quantidade')
        descricao = request.POST.get('descricao')
        imagem_url = request.POST.get('imagem_url')

        # Aqui você poderia criar manualmente o produto
        produto = Produto(
            produto_nome=produto_nome,
            preco=preco,
            produto_quantidade=produto_quantidade,
            descricao=descricao,
            imagem_url=imagem_url
        )
        produto.save()
        return redirect('home')

    return render(request, 'todos/produtos.html')

#lista todos os produtos do banco
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('codproduto')  # Todos os produtos ordenados
    return render(request, 'todos/home.html', {'produtos': produtos})