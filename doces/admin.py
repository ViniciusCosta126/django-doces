from django.contrib import admin
from doces.models import Doce

class DoceAdmin(admin.ModelAdmin):
    list_display = ('nome','valor','descricao')

admin.site.register(Doce,DoceAdmin)
