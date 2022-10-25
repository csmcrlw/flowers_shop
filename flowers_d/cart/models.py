from django.db import models
from bflowers.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False, default=None)
    email = models.EmailField(unique=True, blank=False, default=None)
    phone = PhoneNumberField(unique = True, blank=False, default=None)    # вводить нужно через +7
    address = models.CharField(max_length=255, blank=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.id}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, null=True, blank=True)
    quantity = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.products} - {self.quantity}"

    def total_price(self):
        return self.quantity * self.products.price

    def count_stock(self):
        self.products.stock -= self.quantity