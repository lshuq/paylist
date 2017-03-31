# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='账本名称')),
                ('sum', models.IntegerField(default=0, verbose_name='余额')),
                ('cost', models.IntegerField(default=0, verbose_name='花费')),
                ('lent', models.IntegerField(default=0, verbose_name='借出')),
                ('borrowed', models.IntegerField(default=0, verbose_name='余账')),
            ],
            options={
                'verbose_name_plural': '账本',
                'verbose_name': '账本',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=10, verbose_name='用户')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='person.Page', verbose_name='账本')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]