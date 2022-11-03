from rest_framework import serializers

from api.v1.site.musics.serializers import MusicListSerializer
from music.models import Album


# -------- Album Serializers --------

class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'image',
            'artist',
        ]


# class AlbumCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Album
#         fields = [
#             'id',
#             'name',
#             'image',
#             'artist',
#         ]
#
#
class AlbumDetailSerializer(serializers.ModelSerializer):
    musics = MusicListSerializer(read_only=True, many=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'image',
            'artist',
            'musics',
        ]
#
#
# class AlbumUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Album
#         fields = [
#             'id',
#             'name',
#             'image',
#             'artist',
#         ]

# -------- End Album Serializers --------
