# Generated by Django 5.1.3 on 2024-11-25 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_cliente__saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem_url',
            field=models.URLField(default='http://default.url', max_length=250),
        ),
    ]
