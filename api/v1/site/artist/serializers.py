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
    # first method
    # musics = MusicListSerializer(read_only=True, many=True)
    # albums = AlbumListSerializer(many=True, source='album_set')

    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'photo',
            'bio',
            # 'musics',
            # 'albums',
        ]

    # seconf method qaysi biri yaxshi nima afzalligi bor
    def to_representation(self, instance: Artist):
        response = super().to_representation(instance)
        response['albums'] = instance.album_set.values('id', 'name')
        response['musics'] = instance.musics.values('id', 'name', 'file', 'genre__name')

        return response


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
