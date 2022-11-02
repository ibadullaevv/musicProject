from django.urls import path

from .views import *

urlpatterns = [
    # --------Music --------
    path('list/', ArtistListView.as_view()),
    path('create/', ArtistCreateView.as_view()),
    path('detail/<int:pk>/', ArtistDetailView.as_view()),
    path('update/<int:pk>/', ArtistUpdateView.as_view()),
    path('delete/<int:pk>/', ArtistDeleteView.as_view()),

]
