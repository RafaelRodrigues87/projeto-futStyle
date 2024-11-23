from produto import Preco
class Cliente:
    def __init__(self, cliente_id, cliente_nome, endereco, telefone, email, cpf, data_nascimento, data_cadastro, password, saldo):
        self.cliente_id = cliente_id    
        self.cliente_nome = cliente_nome
        self.endereco = endereco
        self.telefone = telefone
        self._email =  email
        self._cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_cadastro = data_cadastro
        self._password = self._hash_password(password)
        self._saldo = saldo

    @property
    def saldo(self):
        # Retorna o saldo
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        # Verificação simples para garantir que o saldo seja um número e não negativo
        if value < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = value  # Atribui o valor ao atributo privado _saldo

    # Getter e Setter para email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value 

    # Getter e Setter para CPF
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    # Setter para senha (sem getter por segurança)
    def _hash_password(self, password):
        # Aqui você pode colocar o algoritmo de hashing real, como bcrypt
        return password[::-1]  # Exemplo simples: invertendo a string

    def set_password(self, password):
        self._password = self._hash_password(password)

    def verify_password(self, password):
        return self._password == self._hash_password(password)

class ClienteVip(Cliente):
    def __init__(self, cliente_id, cliente_nome, endereco, telefone, email, cpf, data_nascimento, data_cadastro, password, saldo, beneficios):
        # Chama o construtor da classe pai (Cliente)
        super().__init__(cliente_id, cliente_nome, endereco, telefone, email, cpf, data_nascimento, data_cadastro, password, saldo)
        self.beneficios = beneficios  # Atributo exclusivo para ClienteVip

    def Desconto(self):
       return Preco - (Preco * 0.1)
    
print(ClienteVip.Desconto(Preco))