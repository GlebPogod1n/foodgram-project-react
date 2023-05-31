from django.core.validators import MinValueValidator
from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              ImageField, IntegerField, ManyToManyField, Model,
                              SlugField, TextField, UniqueConstraint)

from users.models import User


class Tag(Model):
    name = CharField(
        'Название тега',
        max_length=200,
        unique=True,
    )
    color = CharField(
        'Цветовой HEX-код',
        max_length=7,
        unique=True,
    )
    slug = SlugField(
        'Slug тега',
        max_length=200,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(Model):
    name = CharField(
        'Название',
        max_length=200
    )
    measurement_unit = CharField(
        'Единица измерения',
        max_length=200
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(Model):
    name = CharField(
        'Название',
        max_length=200
    )
    text = TextField(
        'Описание'
    )
    cooking_time = IntegerField(
        'Время приготовления, мин',
        validators=[MinValueValidator(1)]
    )
    image = ImageField(
        'Картинка',
        upload_to='recipes/',
        blank=True
    )
    pub_date = DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    ingredients = ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name='Ингредиенты',
        through='IngredientAmount',
        through_fields=('recipe', 'ingredient'),
    )
    tags = ManyToManyField(
        Tag,
        verbose_name='Теги'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(Model):
    recipe = ForeignKey(
        Recipe,
        on_delete=CASCADE,
        related_name='recipe',
    )
    ingredient = ForeignKey(
        Ingredient,
        on_delete=CASCADE,
        related_name='ingredient',
    )
    amount = IntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='unique ingredient')]

    def __str__(self):
        return (f'В рецепте {self.recipe.name} {self.amount} '
                f'{self.ingredient.measurement_unit} {self.ingredient.name}')


class Favorite(Model):
    recipe = ForeignKey(
        verbose_name='Понравившиеся рецепты',
        related_name='favorite_recipe',
        to=Recipe,
        on_delete=CASCADE,
    )
    user = ForeignKey(
        verbose_name='Пользователь',
        related_name='favorites',
        to=User,
        on_delete=CASCADE,
    )
    date_added = DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        constraints = (
            UniqueConstraint(
                fields=('recipe', 'user', ),
                name='\n%(app_label)s_%(class)s recipe is favorite alredy\n',
            ),
        )

    def __str__(self) -> str:
        return f'{self.user} -> {self.recipe}'


class ShoppingCart(Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='shopping_user',
        verbose_name='Добавил в корзину'
    )
    recipe = ForeignKey(
        Recipe,
        on_delete=CASCADE,
        related_name='shopping_recipe',
        verbose_name='Рецепт в корзине'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.recipe.name}'
