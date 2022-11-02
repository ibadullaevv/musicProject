from django.urls import path

from .views import *

urlpatterns = [
    # --------Music --------
    path('list/', GenreListView.as_view()),
    path('create/', GenreCreateView.as_view()),
    path('detail/<int:pk>/', GenreDetailView.as_view()),
    path('update/<int:pk>/', GenreUpdateView.as_view()),
    path('delete/<int:pk>/', GenreDeleteView.as_view()),

]
