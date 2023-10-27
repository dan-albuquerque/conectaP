from django.contrib import admin

#superuser: host
#senha: 123
from .models import Usuario, Projeto, Voluntario, Usuario

class ListandoPerfil(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links =("id", "nome")
    search_fields = ("nome",)

admin.site.register(Usuario, ListandoPerfil)


class ListandoProjeto(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Projeto, ListandoProjeto)

class ListandoVoluntario(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Voluntario)