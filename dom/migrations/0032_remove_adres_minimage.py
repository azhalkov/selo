# Generated by Django 3.1.4 on 2021-02-18 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0031_auto_20210218_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adres',
            name='minimage',
        ),
    ]