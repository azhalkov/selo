from django.db import models
from django.db.models import Q
#  from django.contrib.auth.models import User
#  from django.db.models.signals import post_save
#  from datetime import datetime
from django.urls import reverse
from transliterate import slugify


class CategoriManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
            qs = qs.filter(or_lookup)
        return qs


class Categori(models.Model):
    """Категория обЪекта"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание", max_length=1024, blank=True, null=True)
    slug = models.SlugField('Ссылка', max_length=160, unique=True)
    objects = CategoriManager()  # Установка менеджера для поиска в модель

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # self.slug = '%s_%s_%s_%s' % (self.name, self.street, self.housenumber, self.apartmentnumber)
        self.slug = slugify(self.name)
        super(Categori, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория обЪекта'
        verbose_name_plural = 'Категории обЪектов'
        ordering = ('-name',)


class DomDokument(models.Model):
    name_document = models.CharField('Название документа', max_length=128, blank=True, null=True)
    filedom = models.FileField('Загрузить', upload_to='dom/dokument')
    datepub = models.DateTimeField('Дата копии', auto_now_add=True, )
    slug = models.SlugField('Ссылка', max_length=160, unique=True)

    def __str__(self):
        return '%s ' % self.name_document

    def save(self, *args, **kwargs):
        # self.slug = '%s_%s_%s_%s' % (self.name, self.street, self.housenumber, self.apartmentnumber)
        self.slug = slugify(self.name_document)
        super(DomDokument, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
