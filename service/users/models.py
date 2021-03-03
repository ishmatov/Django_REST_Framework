from django.db import models
from uuid import uuid4


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, )
    username = models.CharField(max_length=64, unique=True, verbose_name='Никнейм',
                                help_text='Введите никнейм нового пользователя', )
    first_name = models.CharField(max_length=64, null=True, blank=True,
                                  verbose_name='Имя пользователя', )
    last_name = models.CharField(max_length=64, null=True, blank=True,
                                 verbose_name='Фамилия пользователя', )
    email = models.EmailField(unique=True, )
    birthday_year = models.PositiveIntegerField(verbose_name='Год рождения',
                                                null=True, blank=True, )
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Опубликовано', )
    changed = models.DateTimeField(auto_now=True, editable=True,
                                   verbose_name='Изменено', )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['-published']
