from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Categori, DomDokument, Articul, Adres, Person, FotoDom


class FotoDomInline(admin.StackedInline):
    model = FotoDom
    extra = 1


class DomDokumentInline(admin.StackedInline):
    model = DomDokument
    extra = 1

class AdresInline(admin.StackedInline):
    model = Adres
    extra = 1

class CategoriInline(admin.StackedInline):
    model = Categori
    extra = 1

class PersonInline(admin.StackedInline):
    model = Person
    extra = 1

@admin.register(Categori)
class CategoriAdmin(admin.ModelAdmin):
    model = Categori
    fields = ['description', 'name', 'slug']
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    # exclude = ('birth_date',)  # исключить поля из показа
    # empty_value_display = '-empty-'

    # list_editable = ['slug',]


class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields = ['famili', 'phone', 'birth_date', 'status', 'zadachi', 'descreption', 'ispolneno', 'nado' ]
    list_display = ('famili', 'phone', 'status', 'zadachi' , 'ispolneno', 'nado')

admin.site.register(Person, PersonAdmin)


class DomDokumentAdmin(admin.ModelAdmin):
    model = Categori
    list_display = ('name_document', 'filedom', 'datepub', 'slug')
    prepopulated_fields = {"slug": ("name_document",)}


admin.site.register(DomDokument, DomDokumentAdmin)


class ArticulAdmin(admin.ModelAdmin):
    model = Articul
    fieldsets = (
        (None, {'fields': ('tags',)}),
    )
    exclude = ['',]
    list_display = ('art',)
    inlines = [DomDokumentInline, AdresInline, PersonInline, FotoDomInline]

    # prepopulated_fields = {"slug": ("name_document",)}


admin.site.register(Articul, ArticulAdmin)

class AdresAdmin(admin.ModelAdmin):
    model = Adres
    list_display = ('arti_dokument', 'categorii', 'name_krai', 'gorod', 'raion', 'street', 'n_doma','is_prodaju',
                    'is_prodano', 'is_activ', 'n_kvartiri', 'n_podezda',  'is_arenda', 'descreption')
    # inlines = [PersonInline,]
    # list_editable = ('is_activ', 'is_prodaju', 'is_prodano',)


admin.site.register(Adres, AdresAdmin)

class AdminSearchResultsView(admin.ModelAdmin):
    model = Articul

    fields = ['art', 'region', 'nomer']


# admin.site.register(Articul, AdminSearchResultsView)


class FotoDomAdmin(admin.ModelAdmin):
    model = FotoDom
    fields = [ 'title', 'description', 'image', 'movie']

admin.site.register(FotoDom, FotoDomAdmin)

