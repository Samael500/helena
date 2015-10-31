# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galleries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('description', models.TextField(null=True, verbose_name='Описание', blank=True)),
                ('image', models.ImageField(null=True, verbose_name='Изображение', blank=True, upload_to=content.models.ImgWithDescr.get_image_path)),
                ('external_img', models.URLField(null=True, verbose_name='Изображение во внешнем источнике', blank=True)),
            ],
            options={
                'verbose_name': 'изображение в галлерее',
                'verbose_name_plural': 'изображения в галлерее',
            },
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'жанр', 'verbose_name_plural': 'жанры'},
        ),
        migrations.AlterField(
            model_name='genres',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='image',
            field=models.ImageField(null=True, verbose_name='Изображение', blank=True, upload_to=content.models.ImgWithDescr.get_image_path),
        ),
    ]
