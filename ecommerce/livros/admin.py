from django.contrib import admin
from .models import Livro, Autor, Categoria, LivroAutor

class LivroAutorInline(admin.TabularInline):
    model = LivroAutor
    extra = 1

class LivroAdmin(admin.ModelAdmin):
    inlines = [LivroAutorInline]

admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor)
admin.site.register(Categoria)
