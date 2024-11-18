from django.shortcuts import render

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