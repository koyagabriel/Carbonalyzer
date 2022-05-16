import django_filters
from django_filters import rest_framework as filters
from api.models import (Usage, UsageType)


class UsageTypeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = UsageType
        fields = ['unit', 'factor']


class UsageFilter(filters.FilterSet):
    time_range = filters.DateTimeFromToRangeFilter(field_name='usage_at', lookup_expr='range')
    date_range = django_filters.DateFromToRangeFilter(field_name='usage_at', lookup_expr='range')

    class Meta:
        model = Usage
        fields = ['amount', 'usage_at']

