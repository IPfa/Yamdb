import datetime as dt

from django.core.exceptions import ValidationError

UNVALID_SCORE_MESSAGE = ('Оценка произведения должна '
                         'быть в диапазоне от 1 до 10')

UNIQUE_REVIEW_VALIDATION_MESSAGE = ('Можно добавить только один '
                                    'отзыв на произведение')

UNVALID_YEAR_MESSAGE = ('Произведение еще не вышло')


def score_validation(value):
    if value < 1 or value > 10:
        raise ValidationError(UNVALID_SCORE_MESSAGE)
    return value


def year_validation(value):
    year = dt.date.today().year
    if value > year:
        raise ValidationError(UNVALID_SCORE_MESSAGE)
    return value
