from rest_framework import serializers
from bflowers import models

class Product(serializers.ModelSerializer):
    display = serializers.SerializerMethodField()
    class Meta:
        model = models.Product
        fields = '__all__'

    def get_display(self, obj: models.Product) -> str:
        return f'{obj.id}. {obj.name}'


class Category(serializers.ModelSerializer):
    display = serializers.SerializerMethodField()
    class Meta:
        model = models.Category
        fields = '__all__'

    def get_display(self, obj: models.Category) -> str:
        return f'{obj.id}. {obj.name}'