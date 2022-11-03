from rest_framework import serializers

from api.v1.site.musics.serializers import MusicListSerializer
from music.models import Genre


# -------- Genre Serializers --------

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
        ]


# class GenreCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = [
#             'id',
#             'name',
#         ]
#
#
# class GenreDetailSerializer(serializers.ModelSerializer):
#     musics = MusicListSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Genre
#         fields = [
#             'id',
#             'name',
#             'musics',
#         ]
#
#
# class GenreUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = [
#             'id',
#             'name',
#         ]

# -------- End Genre Serializers --------
