from rest_framework import routers
from . import views

app_name = 'music'

router = routers.DefaultRouter()
router.register(r'', views.GenreViewSet, basename="genre")

urlpatterns = router.urls

# urlpatterns = [
#     # --------Music --------
#     path('genres/', GenreViewSet.as_view()),
#     # path('list/', GenreListView.as_view()),
#     # path('create/', GenreCreateView.as_view()),
#     # path('detail/<int:pk>/', GenreDetailView.as_view()),
#     # path('update/<int:pk>/', GenreUpdateView.as_view()),
#     # path('delete/<int:pk>/', GenreDeleteView.as_view()),
#
# ]
