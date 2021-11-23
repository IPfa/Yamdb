# Generated by Django 2.2.16 on 2021-10-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211019_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('anonymous', 'Анонимный'), ('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=9, verbose_name='Тип пользователя'),
        ),
    ]
