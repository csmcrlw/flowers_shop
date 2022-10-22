from django.contrib import admin
from django.contrib import admin
from bflowers import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ('name', )
    search_field = ('name', )
