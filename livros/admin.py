from django.contrib import admin
from .models import Autor, Livro


class LivroInLineAdmin(admin.TabularInline):
    model = Livro


class AutorAdmin(admin.ModelAdmin):
    inlines = [LivroInLineAdmin]


admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro)
