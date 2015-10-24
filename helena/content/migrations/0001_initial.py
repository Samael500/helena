# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(verbose_name='Изображение пример', upload_to=content.models.Genres.get_image_path)),
            ],
        ),
    ]
