from django.db import models
from django.urls import reverse


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artist(Base):
    name = models.CharField('Name artist', max_length=100)
    photo = models.ImageField(upload_to='images/artist/', blank=True)
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])

    class Meta:
        db_table = 'artists'
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'genres'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def get_musics(self):
        """Get music this genre"""
        return self.musics.all()

    def __str__(self):
        return self.name


class Album(Base):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/album/')
    artist = models.ManyToManyField(Artist)

    class Meta:
        db_table = 'albums'

    def get_musics(self):
        """Get music this album"""
        return self.musics.all()

    def __str__(self):
        return self.name


class Music(Base):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/music/')
    genre = models.ForeignKey(Genre, related_name='musics', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE, null=True, blank=True)
    artist = models.ManyToManyField(Artist, related_name='musics', blank=True)

    def __str__(self):
        return self.name
