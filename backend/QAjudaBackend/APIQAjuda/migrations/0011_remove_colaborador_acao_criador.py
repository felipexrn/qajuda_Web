# Generated by Django 4.2.6 on 2023-10-25 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIQAjuda', '0010_colaborador_acao_criador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador_acao',
            name='criador',
        ),
    ]