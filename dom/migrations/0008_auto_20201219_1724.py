# Generated by Django 3.1.4 on 2020-12-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0007_adres'),
    ]

    operations = [
        migrations.AddField(
            model_name='adres',
            name='is_activ',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='На сайте'),
        ),
        migrations.AddField(
            model_name='adres',
            name='is_prodaju',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Продается'),
        ),
        migrations.AddField(
            model_name='adres',
            name='is_prodano',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Продано'),
        ),
        migrations.AddField(
            model_name='adres',
            name='n_doma',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='№ дома'),
        ),
        migrations.AddField(
            model_name='adres',
            name='n_kvartiri',
            field=models.CharField(blank=True, default=0, max_length=128, null=True, verbose_name='№ квартиры'),
        ),
        migrations.AddField(
            model_name='adres',
            name='n_podezda',
            field=models.CharField(blank=True, default=0, max_length=128, null=True, verbose_name='№ подъезда'),
        ),
    ]
