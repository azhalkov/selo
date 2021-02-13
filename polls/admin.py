from django.contrib import admin

from .models import Question, Choice


class ChoiseInlin(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Новый вопрос', {'fields': ['question_text']}),
        ('Информация о дате', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiseInlin]



admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text']
    readonly_fields = ['votes',]

admin.site.register(Choice, ChoiceAdmin)