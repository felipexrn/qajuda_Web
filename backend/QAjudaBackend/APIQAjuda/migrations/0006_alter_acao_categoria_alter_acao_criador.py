# Generated by Django 4.2.6 on 2023-10-25 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIQAjuda', '0005_alter_acao_categoria_alter_acao_criador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIQAjuda.categoria'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='criador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIQAjuda.colaborador'),
        ),
    ]