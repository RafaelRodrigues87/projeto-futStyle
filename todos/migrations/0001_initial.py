# Generated by Django 5.1.3 on 2024-11-23 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente_nome', models.CharField(max_length=255)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimento', models.DateField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=128)),
                ('_saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codproduto', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto_quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('produto_nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteVip',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todos.cliente')),
            ],
            bases=('todos.cliente',),
        ),
    ]
