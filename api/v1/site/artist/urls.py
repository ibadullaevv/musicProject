from rest_framework import routers
from . import views

app_name = 'music'

router = routers.DefaultRouter()
router.register(r'', views.ArtistViewSet, basename="artist")  # NOQA

urlpatterns = router.urls
# urlpatterns = [
#     # --------Music --------
#     path('list/', ArtistListView.as_view()),
#     path('create/', ArtistCreateView.as_view()),
#     path('detail/<int:pk>/', ArtistDetailView.as_view()),
#     path('update/<int:pk>/', ArtistUpdateView.as_view()),
#     path('delete/<int:pk>/', ArtistDeleteView.as_view()),
#
# ]
