# Generated by Django 3.1.4 on 2021-01-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0021_auto_20210104_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adres',
            name='prof',
        ),
        migrations.AddField(
            model_name='person',
            name='artikyl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dom.articul', verbose_name='Участники'),
        ),
    ]
