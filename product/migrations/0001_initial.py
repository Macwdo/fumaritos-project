# Generated by Django 4.1.1 on 2022-09-15 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produtoinfo', models.CharField(max_length=60)),
                ('quantidade', models.CharField(max_length=2)),
                ('dia', models.CharField(max_length=12)),
                ('hora', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=31)),
                ('puffs', models.CharField(max_length=4)),
                ('sabor', models.CharField(max_length=100)),
                ('custo', models.FloatField()),
                ('preco', models.FloatField()),
                ('estoque', models.IntegerField()),
                ('vendidos', models.IntegerField(default=0)),
            ],
        ),
    ]