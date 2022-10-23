from django.urls import path
from bflowers import views
from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('products', views.ProductViewSet, basename='product')
urlpatterns += router.urls