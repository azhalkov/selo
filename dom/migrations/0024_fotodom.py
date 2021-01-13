# Generated by Django 3.1.4 on 2021-01-12 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0023_auto_20210112_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoDom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='dom/images/%Y/%m/%d/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dom.articul', verbose_name='Артикул')),
            ],
            options={
                'verbose_name': 'Фото дома',
                'verbose_name_plural': 'Фото домов',
            },
        ),
    ]
