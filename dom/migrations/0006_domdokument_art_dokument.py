# Generated by Django 3.1.4 on 2020-12-18 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0005_auto_20201218_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='domdokument',
            name='art_dokument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dom.articul', verbose_name='artic'),
        ),
    ]
