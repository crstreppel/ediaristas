# Generated by Django 3.2.6 on 2021-08-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0002_auto_20210829_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='porcentagem_comissao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_banheiro',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_cozinha',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_minimo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_outros',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quarto',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quintal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_sala',
            field=models.FloatField(),
        ),
    ]
