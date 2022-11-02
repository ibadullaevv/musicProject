from django.urls import path, include

urlpatterns = [

    path('music/', include('api.v1.site.musics.urls')),
    path('genre/', include('api.v1.site.genre.urls')),
    path('artist/', include('api.v1.site.artist.urls')),
    path('album/', include('api.v1.site.album.urls'))

]
