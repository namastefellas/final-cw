from django.db import models
from django.contrib.auth import get_user_model

class Advert(models.Model):
    CHOICES = (
        ('Computers', 'Компьютеры'),
        ('Cars', 'Автомобили'),
        ('Other', 'Другое')
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    publicated_at = models.DateTimeField(
        blank=True,
        null=True
    )
    moderated_at = models.BooleanField(
        default=False
        )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=False,
        related_name='advert',
        verbose_name='Пользователь'
    )
    picture = models.ImageField(
        upload_to='pictures',
        verbose_name=('Картинки'),
        blank=True
    )
    title = models.CharField(
        max_length=500,
        blank=False,
        null=False,
        verbose_name=('Заголовок объявления'),
        )
    text = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name=('Текст объявления')
    )
    category = models.CharField(
        max_length=300,
        choices=CHOICES
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'adverts'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        permissions = [
        ('moderate', 'Moderated user or not')
    ]