from rest_framework import serializers

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


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'image',
            'artist',
        ]


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'image',
            'artist',
        ]


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'image',
            'artist',
        ]

# -------- End Album Serializers --------
