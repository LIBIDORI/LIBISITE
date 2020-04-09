# Generated by Django 3.0.4 on 2020-04-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libiapp', '0004_auto_20200403_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='cpostal',
            field=models.CharField(blank=True, max_length=5, verbose_name='Código Postal'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='apellidos',
            field=models.CharField(max_length=100, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='numero',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Número'),
        ),
    ]
