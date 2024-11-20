from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.usuario.username}" if self.usuario else "Carrinho Anônimo"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantidade * self.produto.preco

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Produto, Carrinho, ItemCarrinho

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.user.is_authenticated:
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    else:
        carrinho, _ = Carrinho.objects.get_or_create(usuario=None)  # Carrinho anônimo

    item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not criado:
        item.quantidade += 1
        item.save()

    return JsonResponse({'message': 'Produto adicionado ao carrinho com sucesso'})

from django.shortcuts import render

def ver_carrinho(request):
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
        itens = carrinho.itens.all() if carrinho else []
    else:
        itens = []  # Para carrinho anônimo, podemos usar sessão ou lógica alternativa.

    return render(request, 'carrinho.html', {'itens': itens})

def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return JsonResponse({'message': 'Item removido com sucesso'})

from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    # Para usuários não autenticados, usar a sessão
    if not request.user.is_authenticated:
        carrinho = request.session.get('carrinho', [])
        carrinho.append(produto.id)
        request.session['carrinho'] = carrinho
        return JsonResponse({'message': 'Produto adicionado ao carrinho'})
    
    # Código para usuários autenticados
