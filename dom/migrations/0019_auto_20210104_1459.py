# Generated by Django 3.1.4 on 2021-01-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0018_person_famili'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='descreption',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Задача'),
        ),
    ]
