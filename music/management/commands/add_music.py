from django.core.management.base import BaseCommand
from django.template.defaultfilters import random

from music.models import Music, Genre, Album, Artist


class Command(BaseCommand):
    help = 'Randomly music creating'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, nargs='?', default=1)

    def handle(self, *args, **options):
        quantity = options.get('quantity')
        artist, album = self.get_params()

        for i in range(quantity):
            genre = random(Genre.objects.all())
            music = random(Music.objects.all())
            self.create_music(music, genre, artist, album)

    @staticmethod
    def create_music(music, genre, artist, album):
        """Added music in db"""

        music.id = None
        music.genre = genre
        music.album = album
        music.save()
        music.artist.add(artist)

    @staticmethod
    def get_params() -> tuple:
        """Return randoms instances"""

        album = random(Album.objects.all())
        artist = random(Artist.objects.all())

        return artist, album
