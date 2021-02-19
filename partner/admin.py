from django.contrib import admin
from . models import Usluga


class UslugaAdmin(admin.ModelAdmin):
    model = Usluga

    exclude = [""]

admin.site.register(Usluga, UslugaAdmin)