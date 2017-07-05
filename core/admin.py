from django.contrib import admin
from .models import Convidado

class ConvidadoAdmin(admin.ModelAdmin):
    exclude = ('data_cadastro', )

admin.site.register(Convidado, ConvidadoAdmin)