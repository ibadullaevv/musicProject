from django.core.management.base import BaseCommand
from django.template.defaultfilters import random

from music.models import Music, Genre, Album, Artist


class Command(BaseCommand):
    help = 'Randomly music creating'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        # quantity = options.get('quantity') if 'quantity' in options else 1
        quantity = options.get('quantity')

        for i in range(quantity):
            music = random(Music.objects.all())
            genre = random(Genre.objects.all())
            artist = random(Artist.objects.all())
            album = random(Album.objects.all())

            music.id = None
            music.genre = genre
            music.album = album
            music.save()
            music.artist.add(artist)
