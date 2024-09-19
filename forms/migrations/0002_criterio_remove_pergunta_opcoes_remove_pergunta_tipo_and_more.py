# Generated by Django 5.1 on 2024-09-18 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='opcoes',
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='tipo',
        ),
        migrations.AddField(
            model_name='opcoes',
            name='pergunta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.pergunta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opcoes',
            name='criterio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.criterio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pergunta',
            name='criterio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.criterio'),
            preserve_default=False,
        ),
    ]