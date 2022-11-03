from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    http_method_names = ('get',)

    def list(self, request):
        query_set = Genre.objects.all()
        return Response(self.serializer_class(query_set, many=True).data,
                        status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)

# -------Genre Views ----------
# class GenreListView(ListAPIView):
#     serializer_class = GenreListSerializer
#     queryset = Genre.objects.all().order_by('-id')
#
#
# class GenreCreateView(CreateAPIView):
#     serializer_class = GenreCreateSerializer
#
#
# class GenreDetailView(RetrieveAPIView):
#     serializer_class = GenreDetailSerializer
#     queryset = Genre.objects.all()
#
#
# class GenreUpdateView(UpdateAPIView):
#     serializer_class = GenreListSerializer
#     queryset = Genre.objects.all()
#
#
# class GenreDeleteView(DestroyAPIView):
#     queryset = Genre.objects.all()

# ---------End  Genre  Views-------------
