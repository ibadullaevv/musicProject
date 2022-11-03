from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializer
    http_method_names = ('get',)

    def list(self, request):
        query_set = Album.objects.all()
        return Response(self.serializer_class(query_set, many=True).data,
                        status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)

# -------Album Views ----------
# class AlbumListView(ListAPIView):
#     serializer_class = AlbumListSerializer
#     queryset = Album.objects.all().order_by('-id')
#
#
# class AlbumCreateView(CreateAPIView):
#     serializer_class = AlbumCreateSerializer
#
#
# class AlbumDetailView(RetrieveAPIView):
#     serializer_class = AlbumDetailSerializer
#     queryset = Album.objects.all()
#
#
# class AlbumUpdateView(UpdateAPIView):
#     serializer_class = AlbumUpdateSerializer
#     queryset = Album.objects.all()
#
#
# class AlbumDeleteView(DestroyAPIView):
#     queryset = Album.objects.all()

# ---------End  Album  Views-------------
