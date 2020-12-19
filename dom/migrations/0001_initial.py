# Generated by Django 3.1.4 on 2020-12-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория обЪекта',
                'verbose_name_plural': 'Категории обЪектов',
                'ordering': ('-name',),
            },
        ),
    ]
