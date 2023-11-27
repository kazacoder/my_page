from django.contrib import admin, messages
from django.db.models import QuerySet
from .models import Movie, Director, Actor, DressingRoom


class RatingFilter(admin.SimpleListFilter):
    title = 'фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'низкий'),
            ('40-59', 'Средний'),
            ('60-79', 'Высокий'),
            ('>=80', 'Топ'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40-59':
            return queryset.filter(rating__lt=60, rating__gte=40)
        if self.value() == '60-79':
            return queryset.filter(rating__lt=80, rating__gte=60)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'year', 'currency', 'budget', 'rating']
    # exclude = ['slug']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['year']
    list_display = ['name', 'rating', 'year', 'rating_status', 'director']
    list_editable = ['rating', 'year', 'director']
    filter_horizontal = ['actors']
    ordering = ['rating', 'name']
    list_per_page = 10                          # пагинация
    actions = ['set_dollars', 'set_eur']
    search_fields = ['name', 'year']
    list_filter = ['name', 'year', RatingFilter ]

    @admin.display(ordering='rating', description='Cтатус')
    def rating_status(self, movie: Movie):
        if movie.rating <= 50:
            return 'Фильм так себе'
        if movie.rating < 70:
            return 'Разок посмототреть'
        if movie.rating < 85:
            return 'Зачет'
        else:
            return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(request, f'Было обновлено {count_updated} записей')

    @admin.action(description='Установить валюту в Евро')
    def set_eur(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновлено {count_updated} записей', messages.ERROR)

# admin.site.register(Movie, MovieAdmin) - заменено на декоратор


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'email']
    list_editable = ['last_name', 'first_name', 'email']
    ordering = ['last_name']
    search_fields = ['last_name']
    list_filter = ['last_name']


admin.site.register(Actor)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'floor', 'actor']
    list_editable = ['number', 'floor']
