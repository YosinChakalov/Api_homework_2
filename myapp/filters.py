from django.db.models import Q

def search_filter(queryset, params):
    query = params.get('search')
    if query:
        if queryset.model.__name__ == 'Student':
            return queryset.filter(full_name__icontains=query)
        elif queryset.model.__name__ == 'Course':
            return queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
    return queryset