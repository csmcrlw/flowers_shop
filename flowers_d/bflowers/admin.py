from django.contrib import admin
from bflowers import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    search_field = ('name', )
    list_display = ['name', 'slug', 'price', 'stock', 'available']
    list_filter = ('available', )
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
