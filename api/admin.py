from django.contrib import admin

from reviews.models import Catergory, Comment, Genre, Review, Title

# с другим расположением импортов нас не пускают на сдачу тесты Практикума


EMPTY = '-пусто-'


@admin.register(Catergory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pk')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pk')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'description',
        'category',
        'pk'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'score', 'text')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = EMPTY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'pub_date', 'text')
    search_fields = ('review',)
    list_filter = ('review',)
    empty_value_display = EMPTY
