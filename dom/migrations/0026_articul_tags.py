# Generated by Django 3.1.4 on 2021-02-15 09:42

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('dom', '0025_auto_20210213_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='articul',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]