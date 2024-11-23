class Produto:
    def __init__(self, produto_nome, codproduto, preco, descricao, produto_quantidade):
        self._codproduto = codproduto
        self._preco = preco
        self._produto_quantidade = produto_quantidade
        self._descricao = descricao
        self._produto_nome = produto_nome

    # Getters
    @property
    def CodProduto(self):
        return self._codproduto 
    
    @property
    def Produto_nome(self):
        return self._produto_nome

    # Setter para o código do produto
    @CodProduto.setter
    def CodProduto(self, Codproduto):
        self._codproduto = Codproduto

    # Getters simples sem setter necessário
    @property
    def Preco(self):
        return self._preco
    
    @property
    def Produto_quantidade(self):
        return self._produto_quantidade
    
    @property
    def Descricao(self):
        return self._descricao
    
Preco = 500
