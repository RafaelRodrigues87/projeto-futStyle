from django.db import models 
from django.contrib.auth.hashers import make_password
from .models_produto import Produto
# Create your models here.

class Cliente(models.Model):
    cliente_id = models.AutoField( primary_key=True)
    cliente_nome = models.CharField(max_length=255)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True) #formato 000.000.000-00
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128)
    _saldo = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=500.00)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value < 0:
            raise ValueError("O saldo não pode ser negativo!")
        self._saldo = value

    def save(self, *args, **kwargs):
        if not self.pk: # Somente aplica o hash ao criar, não ao atualizar
            self.password = make_password(self.password)   # Aplica a criptografia na senha
        super().save(*args, **kwargs) # Chama o método save original da classe pai (Model)

class ClienteVip(Cliente):
    # Método para calcular o desconto em um produto
    def desconto(self, produto):
        # Verifica se o argumento é uma instância de Produto
        if isinstance(produto, Produto):
            # Calcula o desconto de 20% no preço do produto
            return produto.preco - (produto.preco * 0.2)
        else:
            raise ValueError("O argumento deve ser uma instância de Produto.")
        
