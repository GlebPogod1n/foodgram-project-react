from django.contrib.auth.models import AbstractUser
from django.db.models import (CASCADE, CharField, EmailField, ForeignKey,
                              Model, UniqueConstraint)


class User(AbstractUser):
    username = CharField(
        verbose_name='Логин',
        max_length=150,
        unique=True,
    )
    first_name = CharField(
        max_length=150,
        verbose_name='Имя',
        blank=True
    )

    last_name = CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=True
    )

    email = EmailField(
        max_length=254,
        verbose_name='email',
        unique=True,
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}, {self.email}'


class Subscribe(Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик'
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='subscribing',
        verbose_name='Подписан'
    )

    def __str__(self):
        return f'{self.user.username} - {self.author.username}'

    class Meta:
        verbose_name = 'Подписка на авторов'
        verbose_name_plural = 'Подписки на авторов'
        constraints = [
            UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'
            )
        ]
