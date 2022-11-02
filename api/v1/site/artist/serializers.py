from rest_framework import serializers

from music.models import Artist


# -------- Artist Serializers --------

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'photo',
            'bio',
        ]


class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'photo',
            'bio',
        ]


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'photo',
            'bio',
        ]


class ArtistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'photo',
            'bio',
        ]

# -------- End Artist Serializers --------
