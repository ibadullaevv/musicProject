from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    path('', views.home, name='home'),
    path('musics/', views.MusicListView.as_view(), name='musics'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre'),
]