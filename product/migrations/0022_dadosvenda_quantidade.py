# Generated by Django 4.1.1 on 2022-09-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_produto_custo_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosvenda',
            name='quantidade',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
