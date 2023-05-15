from django.contrib.admin import ModelAdmin, register
from django.db.models import Count

from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'author', 'text', 'pub_date', 'favorite_count'
    )
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags', 'pub_date')
    filter_vertical = ('tags',)
    empy_value_display = '-пусто-'

    def favorite_count(self, obj):
        return obj.obj_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            obj_count=Count("favorite_recipe", distinct=True),
        )


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empy_value_display = '-пусто-'


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'slug'
    )
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empy_value_display = '-пусто-'


@register(Favorite)
class SubscribeAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'recipe'
    )
    search_fields = ('recipe',)
    list_filter = ('id', 'user', 'recipe')
    empy_value_display = '-пусто-'


@register(ShoppingCart)
class ShoppingCartAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    list_editable = ('user', 'recipe')


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    list_display = ('pk', 'recipe', 'ingredient', 'amount')
    list_editable = ('recipe', 'ingredient', 'amount')
