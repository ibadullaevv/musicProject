from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Music, Artist, Album, Genre


def home(request):
    return render(request, 'base.html')


class MusicListView(ListView):
    model = Music
    template_name = 'musics.html'
    context_object_name = 'musics'


class AlbumListView(ListView):
    model = Album
    template_name = 'albums.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album.html'
    context_object_name = 'album'


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist.html'
    context_object_name = 'artist'


class GenreListView(ListView):
    model = Genre
    template_name = 'genres.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre.html'
    context_object_name = 'genre'
