from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from bflowers import serializers
from bflowers import models

class ProductViewSet(ModelViewSet):
    serializer_class = serializers.Product

    def get_queryset(self):
        return models.Product.objects.filter(available=True)

class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.Category

    def get_queryset(self):
        return models.Category.objects.all()

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'bflowers/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'bflowers/product/detail.html',
#                   {'product': product})
