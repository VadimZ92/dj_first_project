from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from advertisements.models import Advertisement
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    created_at = filters.DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at']
