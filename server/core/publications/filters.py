import django_filters
from .models import Publication


class PublicationFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    sources = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.CharFilter(lookup_expr='exact')
    cat = django_filters.NumberFilter(field_name='cat__id')
    authors = django_filters.NumberFilter(field_name='authors__id')
    isWoS_CC = django_filters.BooleanFilter(field_name='WoS_CC')
    isScopus = django_filters.BooleanFilter(field_name='scopus')
    isRINC = django_filters.BooleanFilter(field_name='RINC')

    class Meta:
        model = Publication
        fields = ['title', 'sources', 'publication_year', 'cat', 'authors']
