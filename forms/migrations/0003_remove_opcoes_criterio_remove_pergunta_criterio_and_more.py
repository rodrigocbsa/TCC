# Generated by Django 5.1 on 2024-09-18 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_criterio_remove_pergunta_opcoes_remove_pergunta_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcoes',
            name='criterio',
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='criterio',
        ),
        migrations.DeleteModel(
            name='Criterio',
        ),
    ]
