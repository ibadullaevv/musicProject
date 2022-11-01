from django.contrib import admin
from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'album', 'get_artists', 'file')

    def get_artists(self, obj):
        return "\n".join([a.name for a in obj.artist.all()])


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
