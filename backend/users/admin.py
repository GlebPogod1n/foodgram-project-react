from django.contrib.admin import ModelAdmin, register

from .models import Subscribe, User


@register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email'
    )
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('first_name', 'email')
    empty_value_display = '-пусто-'


@register(Subscribe)
class SubscribeAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'author')
    list_editable = ('user', 'author')
    empty_value_display = '-пусто-'
