from rest_framework import serializers

from music.models import Music, Album, Genre, Artist



# -------- Genre Serializers --------

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
        ]


class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
        ]


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
        ]


class GenreUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
        ]


# -------- End Genre Serializers --------
