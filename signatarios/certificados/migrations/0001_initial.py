# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.IntegerField()),
                ('fecha_emision', models.DateField()),
                ('fecha_revocacion', models.DateField()),
                ('tipo', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Signatario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=1024)),
                ('ip', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='certificado',
            name='estado_id',
            field=models.ForeignKey(to='certificados.Estado'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='proveedor_id',
            field=models.ForeignKey(to='proveedores.Proveedor'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='signatario_id',
            field=models.ForeignKey(to='certificados.Signatario'),
        ),
    ]
