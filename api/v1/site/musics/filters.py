from django_filters import rest_framework, DateFromToRangeFilter

from music.models import Music


class MusicListFilter(rest_framework.FilterSet):
    genre = rest_framework.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Music
        fields = [
            'genre',
        ]
