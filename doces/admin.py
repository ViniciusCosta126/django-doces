from django.contrib import admin
from doces.models import Doce, Categoria

class DoceAdmin(admin.ModelAdmin):
    list_display = ('nome','valor','categoria','descricao')

admin.site.register(Doce,DoceAdmin)
admin.site.register(Categoria)
