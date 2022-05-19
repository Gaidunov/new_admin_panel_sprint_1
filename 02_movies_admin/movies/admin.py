from django.contrib import admin
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
    # Отображение полей в списке
    list_display = ('name', 'description', 'created',)
    # Фильтрация в списке
    list_filter = ('name', )
    # Поиск по полям
    search_fields = ('name', 'description',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

    # Отображение полей в списке
    list_display = ('full_name',)
    # Фильтрация в списке
    list_filter = ('full_name', )
    # Поиск по полям
    search_fields = ('full_name', )

class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork

class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork



@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline) 

    # Отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating',)
    # Фильтрация в списке
    list_filter = ('type', 'creation_date', 'rating',)
    # Поиск по полям
    search_fields = ('title', 'description', 'id')