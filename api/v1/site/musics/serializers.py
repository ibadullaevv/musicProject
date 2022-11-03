from rest_framework import serializers

from music.models import Music


# -------- Music Serializers --------

class MusicListSerializer(serializers.ModelSerializer):
    genre = serializers.CharField()
    album = serializers.CharField()
    artist = serializers.StringRelatedField(many=True)

    class Meta:
        model = Music
        fields = [
            'id',
            'name',
            'file',
            'genre',
            'album',
            'artist',
        ]

#
# class MusicCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Music
#         fields = [
#             'id',
#             'name',
#             'file',
#             'genre',
#             'album',
#             'artist',
#         ]
#
#
# class MusicDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Music
#         fields = [
#             'id',
#             'name',
#             'file',
#             'genre',
#             'album',
#             'artist',
#         ]
#
#
# class MusicUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Music
#         fields = [
#             'id',
#             'name',
#             'file',
#             'genre',
#             'album',
#             'artist',
#         ]

# -------- End Music Serializers --------
