# Generated by Django 3.0.4 on 2020-03-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='Name',
            new_name='name',
        ),
    ]