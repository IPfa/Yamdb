import textwrap

from django.contrib.auth import get_user_model
from django.db import models
from django.db.utils import IntegrityError

from .validators import UNIQUE_REVIEW_VALIDATION_MESSAGE, score_validation

ERROR_MESSAGES = {'MinValueValidator': 'Записи не должны быть старше 19 века',
                  'MaxValueValidator': 'Треки не должны быть из будущего'}

User = get_user_model()


class Catergory(models.Model):
    name = models.CharField('Имя Категории', max_length=100)
    slug = models.SlugField('Слаг Категории', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self) -> str:
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField('Имя Жанра', max_length=100)
    slug = models.SlugField('Слаг Жанра', unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self) -> str:
        return f'{self.name}'


class Title(models.Model):
    name = models.CharField('Имя Произведения', max_length=200)
    year = models.PositiveSmallIntegerField('Год Выпуска',
                                            db_index=True,
                                            error_messages=ERROR_MESSAGES)
    description = models.TextField(
        'Описание Произведения',
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр Произведения',
    )
    category = models.ForeignKey(
        Catergory,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория Произведения',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self) -> str:
        return f'{self.name} {self.year}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Отзыв на произведение'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Автор отзыва'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        help_text='Дата публикации отзыва'
    )
    score = models.IntegerField(
        'Оценка',
        help_text='Оценка пользователя',
        validators=(score_validation,)
    )
    text = models.TextField('Текст', help_text='Текст поста')

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def save(self, **kwargs):
        force_insert, using = kwargs.get('force_insert'), kwargs.get('using')
        if force_insert is True and using == 'default':
            if Review.objects.filter(author=self.author,
                                     title=self.title).exists():
                raise IntegrityError(UNIQUE_REVIEW_VALIDATION_MESSAGE)
        return super().save(**kwargs)

    def __str__(self):
        slug = self.author.username
        title = self.title
        res = f'Отзыв пользователя {slug} на произведение {title}:\n'
        shorten_text = textwrap.shorten(
            text=self.text,
            width=30,
            placeholder='...'
        )
        res += f'Текст: {shorten_text}\n'
        res += f'Оценка: {self.score}\n'
        res += self.pub_date.strftime('%b %d, %Y, %H:%M')
        return res


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Комментарии к отзыву'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Автор комментария'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        help_text='Дата добавления комментария'
    )
    text = models.TextField('Текст', help_text='Текст комментария')

    class Meta():
        ordering = ('pub_date', )
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        fullname = self.author.get_full_name()
        slug = self.author.username
        res = f'Комментарий пользователя {fullname} ({slug})\n'
        res += f'Текст: {self.text}\n'
        res += self.pub_date.strftime('%b %d, %Y, %H:%M')
        return res
