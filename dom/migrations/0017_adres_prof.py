# Generated by Django 3.1.4 on 2021-01-04 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0016_person_descreption'),
    ]

    operations = [
        migrations.AddField(
            model_name='adres',
            name='prof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dom.person', verbose_name='Участники'),
        ),
    ]
