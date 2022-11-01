"""
ASGI config for musicProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicProject.settings')

application = get_asgi_application()


# musics = Music.objects.all()
# genres = Genre.objects.all()
# for i in range(0, 10):
#     music = random(musics)
#     ganre = random(genres)
#     artist = random(artists)
#     music.id = None
#     music.genre = genre
#     music.artist.add(artist)
#     music.save()