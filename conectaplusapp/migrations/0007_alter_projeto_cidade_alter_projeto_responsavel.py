# Generated by Django 4.2.6 on 2023-11-01 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conectaplusapp', '0006_remove_message_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='cidade',
            field=models.CharField(choices=[('PE', 'Recife'), ('PE', 'Caruaru'), ('PE', 'Petrolina'), ('SP', 'São Paulo'), ('SP', 'Campinas'), ('SP', 'Guarulhos'), ('RJ', 'Rio de Janeiro'), ('RJ', 'Niterói'), ('RJ', 'São Gonçalo')], default='Recife', max_length=100),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='responsavel',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
