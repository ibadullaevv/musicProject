import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# from .filters import MusicListFilter
from .serializers import *


class MusicListView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicListSerializer
    # filterset_class = MusicListFilter
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['genre', 'artist', 'album']
    filterset_fields = {
        'genre': ["in", "exact"],
        'artist': ["in", "exact"],
        'album': ["in", "exact"],
    }
    http_method_names = ('get',)

# ----Music Views--------
# class MusicListView(ListAPIView):
#     serializer_class = MusicListSerializer
#     queryset = Music.objects.all().order_by('-id')
#
#
# class MusicCreateView(CreateAPIView):
#     serializer_class = MusicCreateSerializer
#
#
# class MusicDetailView(RetrieveAPIView):
#     serializer_class = MusicDetailSerializer
#     queryset = Music.objects.all()
#
#
# class MusicUpdateView(UpdateAPIView):
#     serializer_class = MusicUpdateSerializer
#     queryset = Music.objects.all().order_by('-id')
#
#
# class MusicDeleteView(DestroyAPIView):
#     queryset = Music.objects.all().order_by('-id')


# ---------End  Music  Views-------------
