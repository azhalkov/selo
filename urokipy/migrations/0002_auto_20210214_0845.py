# Generated by Django 3.1.4 on 2021-02-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urokipy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karta',
            name='text',
            field=models.TextField(max_length=200, verbose_name='Текст'),
        ),
    ]
