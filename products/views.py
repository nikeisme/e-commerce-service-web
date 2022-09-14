from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

# from core.permissions import IsAdminOrReadOnly

from products.models import Product
from products.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # 사용자 인증
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [IsAdminUser] # is_staff = True 인 계정에만 권한 부여

