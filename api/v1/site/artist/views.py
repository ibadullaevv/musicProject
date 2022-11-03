from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer
    http_method_names = ('get',)

    def list(self, request):
        query_set = Artist.objects.all()
        return Response(self.serializer_class(query_set, many=True).data,
                        status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)

# ---------Artist Views -----------------
# class ArtistListView(ListAPIView):
#     serializer_class = ArtistListSerializer
#     queryset = Artist.objects.all().order_by('-id')
#
#
# class ArtistCreateView(CreateAPIView):
#     serializer_class = ArtistCreateSerializer
#
#
# class ArtistDetailView(RetrieveAPIView):
#     serializer_class = ArtistDetailSerializer
#     queryset = Artist.objects.all()
#
#
# class ArtistUpdateView(UpdateAPIView):
#     serializer_class = ArtistUpdateSerializer
#     queryset = Artist.objects.all()
#
#
# class ArtistDeleteView(DestroyAPIView):
#     queryset = Artist.objects.all()
# ---------End  Artist  Views-------------
