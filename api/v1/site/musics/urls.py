from django.urls import path
from rest_framework import routers
from . import views
from .views import MusicListView

app_name = 'music'

router = routers.DefaultRouter()
# router.register(r'', views.MusicViewSet, basename="music")  # NOQA

urlpatterns = [
    # --------Music --------
    path('list/', MusicListView.as_view()),
    # path('create/', MusicCreateView.as_view()),
    # path('detail/<int:pk>/', MusicDetailView.as_view()),
    # path('update/<int:pk>/', MusicUpdateView.as_view()),
    # path('delete/<int:pk>/', MusicDeleteView.as_view()),

]

urlpatterns += router.urls