from django.urls import path

from .views import *

urlpatterns = [
    # --------Album --------
    path('list/', AlbumListView.as_view()),
    path('create/', AlbumCreateView.as_view()),
    path('detail/<int:pk>/', AlbumDetailView.as_view()),
    path('update/<int:pk>/', AlbumUpdateView.as_view()),
    path('delete/<int:pk>/', AlbumDeleteView.as_view()),

]
