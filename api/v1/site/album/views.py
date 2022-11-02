from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .serializers import *


# -------Album Views ----------
class AlbumListView(ListAPIView):
    serializer_class = AlbumListSerializer
    queryset = Album.objects.all().order_by('-id')


class AlbumCreateView(CreateAPIView):
    serializer_class = AlbumCreateSerializer


class AlbumDetailView(RetrieveAPIView):
    serializer_class = AlbumDetailSerializer
    queryset = Album.objects.all()


class AlbumUpdateView(UpdateAPIView):
    serializer_class = AlbumUpdateSerializer
    queryset = Album.objects.all()


class AlbumDeleteView(DestroyAPIView):
    queryset = Album.objects.all()

# ---------End  Album  Views-------------
