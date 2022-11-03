from rest_framework import routers
from . import views

app_name = 'music'

router = routers.DefaultRouter()
router.register(r'', views.AlbumViewSet, basename="album")

urlpatterns = router.urls

# urlpatterns = [
#     # --------Album --------
#     path('list/', AlbumListView.as_view()),
#     path('create/', AlbumCreateView.as_view()),
#     path('detail/<int:pk>/', AlbumDetailView.as_view()),
#     path('update/<int:pk>/', AlbumUpdateView.as_view()),
#     path('delete/<int:pk>/', AlbumDeleteView.as_view()),
#
# ]
