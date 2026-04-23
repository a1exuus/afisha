from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_description = models.TextField('Краткое описание', default='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    latitude = models.DecimalField('Широта', max_length=20, max_digits=20, decimal_places=16)
    longitude = models.DecimalField('Долгота', max_length=20, max_digits=20, decimal_places=16)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField('Картинка', upload_to='places/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.place
