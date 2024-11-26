from django.shortcuts import render,redirect, get_object_or_404 # type: ignore
from django.db import connection
from django.http import HttpResponse
# from .forms import ClienteForm, ProdutoForm
from django.contrib.auth.hashers import check_password
from .models import Cliente, Produto
from django.contrib.auth import authenticate, login
from django.contrib import messages
#funcao que define as rotas

#tela inical
def view_inical(request):
    return render(request, 'todos/home.html')

#tela carrinho
#
#tela de login
#
#tela de criaçao
def criar(request):
    return render(request, 'todos/criar.html')

def logout(request):
    logout(request)
    return render('todos/login.hmtl')

def produto(request):
    return render(request, 'todos/produtos.html')

#lista de todos os produtos
def ver_produtos(request):
    try:
        # Usando o cursor para executar o comando SQL diretamente
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM todos_produto;")  # Comando SQL
            produtos = cursor.fetchall()  # Retorna todos os resultados

        context = {'produtos': produtos}  # Passa os produtos para o template
        return render(request, 'todos_produtos.html', context)

    except Exception as e:
        # Caso haja erro ao conectar ou executar a consulta
        return render(request, 'todos_produtos.html', {'erro': str(e)})
    
#lista de todos os cliente
def ver_cliente(request):
    try:
        # Usando o cursor para executar o comando SQL diretamente
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM todos_cliente;")  # Comando SQL
            clientes = cursor.fetchall()  # Retorna todos os resultados

        context = {'clientes': clientes}  # Passa os dados dos clientes para o template
        return render(request, 'todos/todos_cliente.html', context)

    except Exception as e:
        # Caso haja erro ao conectar ou executar a consulta
        return render(request, 'todos/todos_cliente.html', {'erro': str(e)})
    
#deleta item
def deletar_cliente(request, cliente_id):
    try:
        # Abrindo o cursor para executar o comando SQL
        with connection.cursor() as cursor:
            # Comando SQL para deletar o cliente com o cliente_id fornecido
            cursor.execute("DELETE FROM todos_cliente WHERE cliente_id = %s", [cliente_id])
            return redirect('ver_cliente')
    
    except Exception as e:
        # Se ocorrer algum erro, retorna a mensagem de erro
        return print(f"Erro ao deletar cliente: {str(e)}")

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
    produtos = Produto.objects.all().order_by('produto_nome')  # Todos os produtos ordenados
    return render(request, 'todos/home.html', {'produtos': produtos})

#verificaçao de dados {login}
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Busca o cliente pelo e-mail
            cliente = Cliente.objects.get(email=email)

            # Verifica se a senha fornecida corresponde à senha hasheada armazenada no banco
            if check_password(password, cliente.password):  # Verificação de senha hasheada
                # Salvar dados na sessão (opcional)
                request.session['cliente_id'] = cliente.cliente_id  # Usando o campo correto, caso 'cliente_id' seja o campo primário
                request.session['cliente_nome'] = cliente.cliente_nome

                return redirect('home')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Senha incorreta.')
        except Cliente.DoesNotExist:
            messages.error(request, 'E-mail não encontrado.')
    
    return render(request, 'todos/login.html')

# Obtém o produto pelo identificador
def adicionar_ao_carrinho(request, codproduto):
    produto = get_object_or_404(Produto, codproduto=codproduto)

    # Verifica se já existe um carrinho na sessão
    carrinho = request.session.get('carrinho', {})

    # Adiciona ou atualiza o produto no carrinho
    if str(codproduto) in carrinho:
        carrinho[str(codproduto)]['quantidade'] += 1
    else:
        carrinho[str(codproduto)] = {
            'nome': produto.produto_nome,
            'preco': float(produto.preco),
            'quantidade': 1,
            "imagem_url": produto.imagem_url
        }

    # Atualiza o carrinho na sessão
    request.session['carrinho'] = carrinho

    # Redireciona para a página anterior ou para a home
    return redirect('carrinho')
def carrinho(request):
    # Recupera o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Calcula o total do carrinho
    total = sum(item['preco'] * item['quantidade'] for item in carrinho.values())

    return render(request, 'todos/carrinho.html', {
        'carrinho': carrinho,
        'total': total
    })
def remover_do_carrinho(request, codproduto):
    # Obtém o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Verifica se o produto está no carrinho
    if str(codproduto) in carrinho:
        # Remove o produto do carrinho
        del carrinho[str(codproduto)]
        
        # Atualiza a sessão
        request.session['carrinho'] = carrinho

    # Redireciona de volta para a página do carrinho
    return redirect('carrinho')  # 'carrinho' é a URL que exibe o carrinho

def aplicar_desconto(request):
    carrinho = request.session.get('carrinho', {})
    codigo_desconto = request.POST.get('codigo_desconto', '').strip()
    
    # Definindo um desconto fixo baseado no código
    desconto = 0
    if codigo_desconto == "DESCONTO10":
        desconto = 10  # Exemplo de desconto fixo de 10 reais
    
    if codigo_desconto == "20":
        desconto = 20

    # Calculando o total do carrinho
    total_carrinho = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    
    # Aplicando o desconto
    total_com_desconto = total_carrinho - desconto
    
    # Atualizando o contexto com o desconto
    return render(request, 'todos/carrinho.html', {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
        'desconto': desconto,
        'total_com_desconto': total_com_desconto
    })

def atualizar_telefone(request, cliente_id, novo_telefone):
   # SQL para atualizar o telefone
    sql = """
    UPDATE todos_cliente
    SET telefone = %s
    WHERE cliente_id = %s;
    """
    valores = (novo_telefone, cliente_id)

    with connection.cursor() as cursor:
        cursor.execute(sql, valores)

    # Redireciona para a página "todos_clientes" após a atualização
    return redirect("ver_cliente")