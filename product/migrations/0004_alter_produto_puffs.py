# Generated by Django 4.1.1 on 2022-09-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_dashboard_produto_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='puffs',
            field=models.CharField(max_length=10),
        ),
    ]
