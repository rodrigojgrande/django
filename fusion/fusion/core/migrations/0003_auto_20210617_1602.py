# Generated by Django 3.2.4 on 2021-06-17 19:02

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_servico_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='twitter',
            field=models.CharField(default='#', max_length=100, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]
