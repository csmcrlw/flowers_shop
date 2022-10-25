from django.urls import path
from rest_framework import routers
from bflowers import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls