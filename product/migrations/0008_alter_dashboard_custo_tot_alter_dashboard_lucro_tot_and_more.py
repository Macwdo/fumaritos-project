# Generated by Django 4.1.1 on 2022-09-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_dashboard_produto_dashboard_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='custo_tot',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='lucro_tot',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='preco_tot',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='vendidos',
            field=models.FloatField(default=0),
        ),
    ]
