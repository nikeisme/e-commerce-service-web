from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

# from core.permissions import IsAdminOrReadOnly

from products.models import Product
from products.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

