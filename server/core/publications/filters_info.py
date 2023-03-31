from publications.filters import PublicationFilter

def get_filters_info():
    filters_info = []

    for filter_name, filter_obj in PublicationFilter.base_filters.items():
        filter_type = filter_obj.__class__.__name__
        filters_info.append({
            'filter_name': filter_name,
            'filter_type': filter_type
        })

    return filters_info