# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'title')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'date')),
                ('content', models.TextField(null=True, verbose_name=b'content', blank=True)),
            ],
            options={
                'ordering': ['-date_time'],
                'verbose_name': 'article',
                'verbose_name_plural': 'article',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=50, verbose_name=b'tags')),
                ('tag_cn_name', models.CharField(max_length=50, verbose_name=b'chinesename', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', max_length=50, blank=True),
        ),
    ]
