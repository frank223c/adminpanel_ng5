# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0002_auto_20180201_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name='Fecha de última actualización del objeto')),
                ('company_name', models.CharField(max_length=140)),
                ('contact_person', models.CharField(max_length=140)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=140)),
                ('town', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='location.Town')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
