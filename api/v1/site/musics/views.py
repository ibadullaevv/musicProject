from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .serializers import *


# ----Music Views--------
class MusicListView(ListAPIView):
    serializer_class = MusicListSerializer
    queryset = Music.objects.all().order_by('-id')


class MusicCreateView(CreateAPIView):
    serializer_class = MusicCreateSerializer


class MusicDetailView(RetrieveAPIView):
    serializer_class = MusicDetailSerializer
    queryset = Music.objects.all()


class MusicUpdateView(UpdateAPIView):
    serializer_class = MusicUpdateSerializer
    queryset = Music.objects.all().order_by('-id')


class MusicDeleteView(DestroyAPIView):
    queryset = Music.objects.all().order_by('-id')


# ---------End  Music  Views-------------

