from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Karta(models.Model):

    title = models.CharField('Тема', max_length=28)
    image = models.ImageField('Картинка', upload_to='urokipy/images', blank=True, null=True)
    alt = models.CharField('alt', max_length=50, blank=True, null=True)
    text = models.TextField('Текст', max_length=200)
    links = models.URLField('Ссылка', default='#')
    button_text = models.CharField('Текст кнопки', max_length=28)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Памятка'
        verbose_name_plural = 'Памятки'


class Bulma(Karta):
    class Meta:
        verbose_name = 'Карточка bulma'
        verbose_name_plural = 'Памятки bulma'

