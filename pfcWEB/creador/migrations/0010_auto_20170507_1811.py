# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creador', '0009_remove_usuariosapp_listasolicitudes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='solicitudes',
        ),
        migrations.AddField(
            model_name='tareas',
            name='creador',
            field=models.CharField(default='', max_length=100),
        ),
    ]