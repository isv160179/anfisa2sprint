from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField(
        'Цена',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ],
        help_text='Рекомендованная розничная цена',
    )
    comment = models.TextField('Комментарий', blank=True)
    image = models.ImageField('Фото', blank=True, upload_to='proposal_images')

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('contest:detail', kwargs={'pk': self.pk})
