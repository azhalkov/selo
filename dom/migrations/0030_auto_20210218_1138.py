# Generated by Django 3.1.4 on 2021-02-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0029_adres_minimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='minimage',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.related.ForeignKey>', verbose_name='Миниатюра'),
        ),
    ]
