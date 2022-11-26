from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["title", ]
    search_fields = ['id', 'title', 'description']
    ordering_fields = ['id', ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["address", 'id', 'products']
    search_fields = ['id', 'products', "address" ]
    ordering_fields = ['id', ]