from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .serializers import *


# -------Genre Views ----------
class GenreListView(ListAPIView):
    serializer_class = GenreListSerializer
    queryset = Genre.objects.all().order_by('-id')


class GenreCreateView(CreateAPIView):
    serializer_class = GenreCreateSerializer


class GenreDetailView(RetrieveAPIView):
    serializer_class = GenreDetailSerializer
    queryset = Genre.objects.all()


class GenreUpdateView(UpdateAPIView):
    serializer_class = GenreListSerializer
    queryset = Genre.objects.all()


class GenreDeleteView(DestroyAPIView):
    queryset = Genre.objects.all()

# ---------End  Genre  Views-------------
