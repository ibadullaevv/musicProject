from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .serializers import *


# ---------Artist Views -----------------
class ArtistListView(ListAPIView):
    serializer_class = ArtistListSerializer
    queryset = Artist.objects.all().order_by('-id')


class ArtistCreateView(CreateAPIView):
    serializer_class = ArtistCreateSerializer


class ArtistDetailView(RetrieveAPIView):
    serializer_class = ArtistDetailSerializer
    queryset = Artist.objects.all()


class ArtistUpdateView(UpdateAPIView):
    serializer_class = ArtistUpdateSerializer
    queryset = Artist.objects.all()


class ArtistDeleteView(DestroyAPIView):
    queryset = Artist.objects.all()
# ---------End  Artist  Views-------------
