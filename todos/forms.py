from django import forms
from .models import Cliente
from django.http import HttpResponse

# def inserir_cliente(request):
#     cliente = Cliente(
#         cliente_nome='Rafael Rodrigues',
#         email='rafael@example.com',
#         endereco='Rua X, 123',
#         telefone='123456789',
#         cpf='123.456.789-00',
#         data_nascimento='2000-01-01',
#         password='senha123'
#     )
#     cliente.save()
#     return HttpResponse("Cliente inserido com sucesso!")
#criando a classe  do formulario de cadastro do cliente
class ClienteForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())
     
    class Meta:
        model = Cliente
        fields = ['cliente_nome', 'email', 'endereco', 'telefone', 'cpf', 'data_nascimento', 'password']
        #   nao deixa o ver oq esta digitando
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("password")
        confirmar_senha = cleaned_data.get("password_confirm")

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não correspondem.")