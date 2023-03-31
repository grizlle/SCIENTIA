from publications.filters import PublicationFilter
from publications.models import Publication
from django.core.exceptions import FieldDoesNotExist


def get_filters_info():
    filters_info = []

    for filter_name, filter_obj in PublicationFilter.base_filters.items():
        filter_type = filter_obj.__class__.__name__

        try:
            field = Publication._meta.get_field(filter_name)
            verbose_name = field.verbose_name
        except FieldDoesNotExist:
            verbose_name = filter_name

        filters_info.append({
            'filter_name': filter_name,
            'filter_type': filter_type,
            'filter_client_name': verbose_name
        })

    return filters_info