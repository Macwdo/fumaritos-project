# Generated by Django 4.1.1 on 2022-09-24 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprador', models.CharField(default='Não Informado', max_length=60)),
                ('produtoinfo', models.CharField(max_length=68)),
                ('quantidade', models.IntegerField()),
                ('dia', models.CharField(max_length=12)),
                ('hora', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('puffs', models.CharField(max_length=4)),
                ('sabor', models.CharField(max_length=100)),
                ('custo', models.FloatField()),
                ('preco', models.FloatField()),
                ('estoque', models.IntegerField()),
                ('vendidos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DashBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(default='', max_length=30)),
                ('puffs', models.CharField(default='', max_length=4)),
                ('sabor', models.CharField(default='', max_length=100)),
                ('vendidos', models.IntegerField(default=0)),
                ('lucro_tot', models.FloatField(default=0)),
                ('preco_tot', models.FloatField(default=0)),
                ('custo_tot', models.FloatField(default=0)),
                ('produto_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.produto')),
            ],
        ),
    ]
