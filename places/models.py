from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description_short = models.CharField('Краткое описание', max_length=800, default='Краткое описание')
    description_long = models.TextField('Описание', default='Описание')
    lat = models.DecimalField('Широта', max_length=20, max_digits=20, decimal_places=16, default=0.0000000)
    lng = models.DecimalField('Долгота', max_length=20, max_digits=20, decimal_places=16, default=0.0000000)

    def __str__(self):
        return self.title
