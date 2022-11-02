from django.urls import path

from .views import *

urlpatterns = [
    # --------Music --------
    path('list/', MusicListView.as_view()),
    path('create/', MusicCreateView.as_view()),
    path('detail/<int:pk>/', MusicDetailView.as_view()),
    path('update/<int:pk>/', MusicUpdateView.as_view()),
    path('delete/<int:pk>/', MusicDeleteView.as_view()),

]
