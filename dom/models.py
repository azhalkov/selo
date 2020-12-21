from django.db import models
from django.db.models import Q
#  from django.contrib.auth.models import User
#  from django.db.models.signals import post_save
#  from datetime import datetime
from django.urls import reverse
from transliterate import slugify


class Articul(models.Model):
    art = models.CharField('Артикул', max_length=10, unique=True)
    region = models.CharField('Код региона', max_length=3, blank=True, null=True, help_text="Трехзначное число")
    mesto = models.CharField('Местоположение', max_length=2, blank=True, null=True, help_text="Двухзначное число")
    kod_phone = models.CharField('Код телефона', max_length=5, blank=True, null=True, help_text="Пятизначное число")
    nomer = models.CharField('Порядковый номер', max_length=6, blank=True, null=True,
                             help_text="Шестизначное число", default='000000')
    slug = models.SlugField('Уникальная ссылка', max_length=16, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Артикул'
        verbose_name_plural = 'Артикулы'
        ordering = ('-art',)

    def __str__(self):
        return self.art

    def save(self, *args, **kwargs):
        self.slug = '%s_%s_%s_%s' % (self.region, self.mesto, self.kod_phone, self.nomer)
        self.art = self.slug.replace('_', '')
        #self.slug = slugify(self.slug)
        super(Articul, self).save(*args, **kwargs)


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
    art_dokument = models.ForeignKey(Articul, verbose_name='artic', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s ' % self.name_document

    def save(self, *args, **kwargs):
        # self.slug = '%s_%s_%s_%s' % (self.name, self.street, self.housenumber, self.apartmentnumber)
        self.slug = slugify(self.name_document)
        super(DomDokument, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Adres(models.Model):
    """Адрес объекта"""
    name_krai = models.CharField('Край, область', max_length=128)
    gorod = models.CharField('Нас. пункт', max_length=128)
    raion = models.CharField('Район', max_length=128)
    street = models.CharField('Улица', max_length=128)
    n_doma = models.CharField('№ дома', max_length=10, default=0)
    n_kvartiri = models.CharField('№ квартиры', max_length=128, blank=True, null=True, default=0)
    n_podezda = models.CharField('№ подъезда', max_length=128, blank=True, null=True, default=0)
    slug = models.SlugField('Ссылка', max_length=160, unique=True, blank=True, null=True)
    is_activ = models.BooleanField('На сайте', default=False, blank=True, null=True)
    is_prodaju = models.BooleanField('Продается', default=False, blank=True, null=True)
    is_prodano = models.BooleanField('Продано', default=False, blank=True, null=True)
    is_arenda = models.BooleanField('В аренду', default=False, blank=True, null=True)
    descreption = models.TextField('Объявление', max_length=5000, blank=True, null=True)
    arti_dokument = models.ForeignKey(Articul, verbose_name='artic', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s%s ' % (self.gorod,self.arti_dokument)

    def save(self, *args, **kwargs):
        self.slug = '%s_%s' % (self.gorod, self.arti_dokument)
        self.slug = slugify(self.slug)
        super(Adres, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'