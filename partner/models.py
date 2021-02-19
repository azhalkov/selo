""" partner/models"""
from django.db import models

from accounts.models import CustomUser

"""Избегайте использования null для строковых полей таких, как 
CharField и TextField, т.к. пустое значение всегда будет сохранено 
как пустая строка, а не NULL. Если строковое поле содержит null=True,
это означает, что оно может содержать два возможных “пустых” значения:
NULL и пустую строку. В большинстве случаев избыточно иметь два
варианты “пустых” значений. Правило Django использовать пустую строку,
вместо NULL. Для всех типов полей, вы также должны указать blank=True
если вы хотите разрешить пустые значения в формах, т.к. параметр null
влияет только на сохранение в базе данных"""


class Usluga(models.Model):
    template_name = 'partner/uslugi.html'
    gorodok = models.CharField('Населенный пункт', max_length=60, blank=True)
    vid_uslugi = models.CharField("Вид услуги", max_length=96, help_text="Укажите название услуги",
                                  default="Отсутствует")
    ispolnitel = models.ManyToManyField(CustomUser)
    kontakt = models.CharField("Телефон", max_length=12, default="Контактный номер телефона")
    nameurl = models.CharField("Название ссылки", max_length=96, default="Имя ссылки")
    usluga_url = models.URLField("Ссылка", default='Ссылка отсутствует')
    price = models.CharField('Стоимость', max_length=48, blank=True, default='Стоимость зависит от сложности договора')

    def __str__(self):
        return f'{self.vid_uslugi}'

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

