from rest_framework.viewsets import ModelViewSet
from bflowers import serializers
from bflowers import models
from bflowers.permissions import IsAdminOrReadOnly

class ProductViewSet(ModelViewSet):
    serializer_class = serializers.Product
    queryset = models.Product.objects.filter(available=True)
    permission_classes = (IsAdminOrReadOnly, )

class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.Category
    queryset = models.Category.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


