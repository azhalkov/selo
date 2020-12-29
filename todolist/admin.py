from django.contrib import admin

# Register your models here.
from .models import Category, TodoList

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    # fields = ['description', 'name', 'slug']
    # list_display = ('name', 'description', 'slug')
    # prepopulated_fields = {"slug": ("name",)}
    exclude = ['']  # исключить поля из показа
    # empty_value_display = '-empty-'

    # list_editable = ['slug',]


admin.site.register(Category, CategoryAdmin)

class TodoListAdmin(admin.ModelAdmin):
    model = TodoList
    # fields = ['description', 'name', 'slug']
    # list_display = ('name', 'description', 'slug')
    # prepopulated_fields = {"slug": ("name",)}
    exclude = ['']  # исключить поля из показа
    # empty_value_display = '-empty-'

    # list_editable = ['slug',]


admin.site.register(TodoList, TodoListAdmin)
