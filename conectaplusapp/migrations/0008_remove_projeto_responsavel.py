# Generated by Django 4.2.6 on 2023-11-02 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conectaplusapp', '0007_alter_projeto_cidade_alter_projeto_responsavel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='responsavel',
        ),
    ]
