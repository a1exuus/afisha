from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage
import requests
import os


class Command(BaseCommand):
    help = 'Загружает данные о локациях из JSON-файла по ссылке'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        self.stdout.write(
                    self.style.SUCCESS('\nНачинаем загрузку!')
                    )
        url = options['json_url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            raw_place = response.json()

            place_obj, created = Place.objects.get_or_create(
                title=raw_place['title'],
                defaults={
                    'description_short': raw_place.get('description_short'),
                    'description_long': raw_place.get('description_long'),
                    'longitude': raw_place['coordinates']['lng'],
                    'latitude': raw_place['coordinates']['lat'],
                }
            )

            if not created:
                self.stdout.write(f"Место {place_obj.title} уже загружено!")
                return

            if created:
                for number, img_url in enumerate(raw_place['imgs'], 1):
                    response = requests.get(img_url)
                    response.raise_for_status()

                    filename = os.path.basename(img_url)

                    img_instance = PlaceImage(
                        place=place_obj,
                        order=number
                    )

                    img_instance.image.save(
                        filename, ContentFile(response.content), save=True
                        )
                self.stdout.write(
                    self.style.SUCCESS(f"\nСоздано место: {place_obj.title}")
                    )
            else:
                self.stdout.write(f"\nМесто {place_obj.title} уже существует")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n\nОшибка при загрузке: {e}'))
