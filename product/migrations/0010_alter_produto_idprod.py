# Generated by Django 4.1.1 on 2022-09-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_produto_id_remove_produto_slug_produto_idprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='idprod',
            field=models.AutoField(default=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
