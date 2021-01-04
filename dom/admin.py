from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Categori, DomDokument, Articul, Adres


class DomDokumentInline(admin.StackedInline):
    model = DomDokument
    extra = 1

class AdresInline(admin.StackedInline):
    model = Adres
    extra = 1

class CategoriInline(admin.StackedInline):
    model = Categori
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


# admin.site.register(Categori, CategoriAdmin)


class DomDokumentAdmin(admin.ModelAdmin):
    model = Categori
    list_display = ('name_document', 'filedom', 'datepub', 'slug')
    prepopulated_fields = {"slug": ("name_document",)}


admin.site.register(DomDokument, DomDokumentAdmin)


class ArticulAdmin(admin.ModelAdmin):
    model = Articul
    exclude = ['']
    list_display = ('art',)
    inlines = [DomDokumentInline, AdresInline, ]

    # prepopulated_fields = {"slug": ("name_document",)}


admin.site.register(Articul, ArticulAdmin)

class AdresAdmin(admin.ModelAdmin):
    model = Adres
    list_display = ('arti_dokument', 'name_krai', 'gorod', 'raion', 'street', 'n_doma','is_prodaju',
                    'is_prodano', 'is_activ', 'n_kvartiri', 'n_podezda',  'is_arenda', 'descreption')
    # inlines = [CategoriInline,]
    # list_editable = ('is_activ', 'is_prodaju', 'is_prodano',)

admin.site.register(Adres, AdresAdmin)

class AdminSearchResultsView(admin.ModelAdmin):
    model = Articul

    fields = ['art', 'region', 'nomer']