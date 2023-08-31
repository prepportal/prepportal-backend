from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.query import QuerySet

def get_paginated_queryset(queryset: QuerySet, request, search_fields, sort_fields: dict = None) -> dict:
    sort_fields = sort_fields or {}

    page = int(request.query_params.get("pageIndex", 1))
    per_page = int(request.query_params.get("perPage", 10))
    search_query = request.query_params.get("search")
    sort_by = request.query_params.get("sortBy")

    if search_query:
        query = Q()
        for field in search_fields:
            query |= Q(**{f"{field}__icontains": search_query})

        queryset = queryset.filter(query)

    if sort_by:
        sort = sort_by[1:] if sort_by.startswith("-") else sort_by
        if sort_field_name := sort_fields.get(sort):
            if sort_by.startswith("-"):
                sort_field_name = f"-{sort_field_name}"

            queryset = queryset.order_by(sort_field_name)

    paginator = Paginator(queryset, per_page)
    queryset = paginator.get_page(page)

    return {
        "queryset": queryset,
        "pagination": {
            "count": paginator.count,
            "totalPages": paginator.num_pages,
            "isNext": queryset.has_next(),
            "isPrev": queryset.has_previous(),
            "nextPage": queryset.next_page_number() if queryset.has_next() else None,
        },
    }