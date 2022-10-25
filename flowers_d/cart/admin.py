from django.contrib import admin
from .models import Cart, CustomUser

@admin.register(Cart)
class Cart(admin.ModelAdmin):
    search_fields = ('user', 'created')

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
