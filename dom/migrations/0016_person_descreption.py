# Generated by Django 3.1.4 on 2021-01-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0015_auto_20210104_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='descreption',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Задача'),
        ),
    ]