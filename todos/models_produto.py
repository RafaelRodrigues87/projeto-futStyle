from django.db import models


class Produto(models.Model):
    codproduto = models.AutoField(primary_key=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    produto_quantidade = models.IntegerField()
    descricao = models.TextField()
    produto_nome = models.CharField(max_length=80)
    imagem_url = models.URLField(max_length=250, default='http://default.url')  # Novo campo para armazenar a URL da imagem
