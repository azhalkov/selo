from django.utils import timezone  # мы будем получать дату создания todo
from django.db import models


class Category(models.Model):  # Таблица категория которая наследует models.Model
    name = models.CharField(max_length=100)  # varchar.Нам потребуется только имя категории

    class Meta:
        verbose_name = ("Category")  # человекочитаемое имя объекта

    verbose_name_plural = ("Categories")  # человекочитаемое множественное имя для Категорий


    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)  # текстовое поле
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # дата создания
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # до какой даты нужно было сделать дело
    category = models.ForeignKey(Category, default="general",
                                 on_delete=models.PROTECT)  # foreignkey с помощью которой мы будем осуществлять связь с таблицей Категорий

    class Meta:  # используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-created"]  # сортировка дел по времени их создания

    def __str__(self):
        return self.title
