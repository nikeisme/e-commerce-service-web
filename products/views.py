from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

# from core.permissions import IsAdminOrReadOnly

from products.models import Product
from products.permissions import IsSellerOrReadOnly
from products.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsSellerOrReadOnly]  # is_staff = True 인 계정에만 권한 부여

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ProductSerializer
        return ProductSerializer

    # 사용자 인증
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)



