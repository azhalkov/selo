# dom/models
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from transliterate import slugify

from accounts.models import CustomUser


class CategoriManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
            qs = qs.filter(or_lookup)
        return qs


class Articul(models.Model):
    """Планируется как поле для поиска объектов """
    art = models.CharField('Артикул', max_length=16, unique=True, blank=True, null=True)
    region = models.CharField('Код региона', max_length=3, blank=True, null=True, help_text="Трехзначное "
                               "число - Краснодарский край 023 или 123 ")
    mesto = models.CharField('Местоположение', max_length=2, blank=True, null=True, help_text="Двухзначное число")
    kod_phone = models.CharField('Код телефона', max_length=5, blank=True, null=True, help_text="Пятизначное число")
    nomer = models.CharField('Порядковый номер', max_length=6, blank=True, null=True,
                             help_text="Шестизначное число", default='000000')
    slug = models.SlugField('Уникальная ссылка', max_length=19, unique=True, blank=True, null=True)
    objects = CategoriManager()
    tags = TaggableManager(verbose_name="Тэги", blank=True)



    class Meta:
        verbose_name = 'Артикул'
        verbose_name_plural = 'Артикулы'
        ordering = ('-art',)

    def __str__(self):
        return self.art

    def save(self, *args, **kwargs):
        self.slug = '%s%s%s%s' % (self.region, self.mesto, self.kod_phone, self.nomer)
        self.art = self.slug.replace('_', '')

        #self.slug = slugify(self.slug)
        super(Articul, self).save(*args, **kwargs)



class Categori(models.Model):
    """Категория обЪекта"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание", max_length=1024, blank=True, null=True)
    slug = models.SlugField('Ссылка', max_length=160, unique=True)
    art_categori = models.ForeignKey(Articul, verbose_name='Арт_категории', on_delete=models.SET_NULL, null=True)
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


class Person(models.Model):
    CHOICES = (
        ('Pro', 'Продавец'),
        ('Poc', 'Покупатель'),
        ('No', 'Неизвестно'),
        ('Uri', 'Юрист'),
        ('Pom', 'Помошник'),
    )
    pers = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    famili = models.CharField(u'ФИО', max_length=500, blank=True, null=True)
    phone = models.CharField(u'Телефон', max_length=500, blank=True, null=True)
    birth_date = models.DateField(u'День рождения', null=True, blank=True)
    status = models.CharField(u'Статус', max_length=300, choices = CHOICES, default='No')
    zadachi = models.DateField(u'Дата задачи', null=True, blank=True)
    descreption = models.TextField(u'Задача', max_length=500, blank=True, null=True)
    ispolneno = models.BooleanField(u'Исполнено', default=False)
    nado = models.BooleanField(u'В работе', default=False)
    artikyl = models.ForeignKey(Articul, verbose_name=u'Участники', on_delete=models.SET_NULL, null=True)
    objects = CategoriManager()# Установка менеджера для поиска в модель


    def __str__(self):
        return '%s ' % self.famili

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'




class DomDokument(models.Model):

    name_document = models.CharField('Название документа', max_length=128, blank=True, null=True)
    filedom = models.FileField('Загрузить', upload_to='dom/dokument')
    datepub = models.DateTimeField('Дата копии', auto_now_add=True, )
    slug = models.SlugField('Ссылка', max_length=160, unique=True, blank=True, null=True)
    art_dokument = models.ForeignKey(Articul, verbose_name='artic', on_delete=models.SET_NULL, null=True)
    objects = CategoriManager()# Установка менеджера для поиска в модель

    def __str__(self):
        return '%s_%s ' % (self.name_document, self.art_dokument)

    def save(self, *args, **kwargs):
        # self.slug = '%s_%s_%s_%s' % (self.name, self.street, self.housenumber, self.apartmentnumber)
        self.slug = slugify(self.name_document)
        super(DomDokument, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Adres(models.Model):
    """Адрес объекта"""
    price = models.CharField('Цена', max_length=12, default='?')
    name_krai = models.CharField('Край, область', max_length=128)
    gorod = models.CharField('Нас. пункт', max_length=128, )
    raion = models.CharField('Район', max_length=128)
    street = models.CharField('Улица', max_length=128)
    n_doma = models.CharField('№ дома', max_length=10, default='')
    n_kvartiri = models.CharField('№ квартиры', max_length=128, blank=True, null=True, default=0)
    n_podezda = models.CharField('№ подъезда', max_length=128, blank=True, null=True, default=0)
    slug = models.SlugField('Ссылка', max_length=160, unique=True, blank=True, null=True)
    is_activ = models.BooleanField('На сайте', default=False, blank=True, null=True)
    is_prodaju = models.BooleanField('Продается', default=False, blank=True, null=True)
    is_prodano = models.BooleanField('Продано', default=False, blank=True, null=True)
    is_arenda = models.BooleanField('В аренду', default=False, blank=True, null=True)
    descreption = models.TextField('Объявление', max_length=5000, blank=True, null=True)
    arti_dokument = models.ForeignKey(Articul, verbose_name='Артикул', on_delete=models.SET_NULL, null=True)
    categorii = models.ForeignKey(Categori, verbose_name='Категория земель', on_delete=models.SET_NULL, null=True)
    objects = CategoriManager()# Установка менеджера для поиска в модель


    def __str__(self):
        return '%s%s ' % (self.gorod,self.arti_dokument)

    def get_absolute_url(self):
        return reverse('adresa_detail', args=(self.slug,))

    class Meta:
        default_related_name = 'ad_res'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


    def save(self, *args, **kwargs):
        self.slug = '%s_%s' % (self.gorod, self.arti_dokument)
        self.slug = slugify(self.slug)

        super(Adres, self).save(*args, **kwargs)




class FotoDom(models.Model):
    """Фото дома"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True, null=True )
    image = models.ImageField("Изображение", upload_to="dom/images/%Y/%m/%d/", blank=True)
    movie = models.ForeignKey(Articul, verbose_name="Артикул", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото дома"
        verbose_name_plural = "Фото домов"










# from django.db import models
#
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline
#
#



