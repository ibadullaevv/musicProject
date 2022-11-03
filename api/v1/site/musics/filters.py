# from django_filters import rest_framework, DateFromToRangeFilter
# from django.forms.fields import IntegerField, MultipleChoiceField
# from django_filters.filters import Filter
#
# from music.models import Music
#
#
# class MultipleValueField(MultipleChoiceField):
#     def __init__(self, *args, field_class, **kwargs):
#         self.inner_field = field_class()
#         super().__init__(*args, **kwargs)
#
#     def valid_value(self, value):
#         return self.inner_field.validate(value)
#
#     def clean(self, values):
#         return values and [self.inner_field.clean(value) for value in values]
#
#
# class MultipleValueFilter(Filter):
#     field_class = MultipleValueField
#
#     def __init__(self, *args, field_class, **kwargs):
#         kwargs.setdefault('lookup_expr', 'in')
#         super().__init__(*args, field_class=field_class, **kwargs)
#
#
# class MusicListFilter(rest_framework.FilterSet):
#     id = MultipleValueFilter(field_class=IntegerField)
#     # genre = rest_framework.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Music
#         fields = [
#             'id',
#         ]
