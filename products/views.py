from rest_framework import viewsets
from products.models import Product
from products.permissions import IsAdminOrReadOnly
from products.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]  # is_staff = True 인 계정 에만 권한 부여
    serializer_class = ProductSerializer




