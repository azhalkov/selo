from django.db import models
from django.utils import timezone
import datetime





class Question(models.Model):
    question_text = models.CharField('вопрос', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text='Выбирайте вопрос')
    choice_text = models.CharField('Текст ответа', max_length=200)
    votes = models.IntegerField('Количество голосов', default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'