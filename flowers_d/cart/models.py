from django.db import models
from bflowers.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=False, default=None, verbose_name='Фамилия')
    email = models.EmailField(unique=True, blank=False, default=None, verbose_name='Email')
    phone = PhoneNumberField(unique = True, blank=False, default=None, verbose_name='Телефон')    # вводить нужно через +7
    address = models.CharField(max_length=255, blank=False, default=None, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.id}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, null=True, blank=True, verbose_name='Товары')
    quantity = models.IntegerField(null=False, default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_ordered = models.BooleanField(verbose_name='Заказано', default=False)
    is_delivered = models.BooleanField(verbose_name='Доставлено', default=False)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"{self.user} - {self.created_at}"

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Товары')
#
#     def __iter__(self):
#         """
#         Перебор элементов в корзине и получение продуктов из базы данных.
#         """
#         product_ids = self.cart.keys()
#         # получение объектов product и добавление их в корзину
#         products = Product.objects.filter(id__in=product_ids)
#         for product in products:
#             self.cart[str(product.id)]['product'] = product
#
#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item
#
#     def __len__(self):
#         """
#         Подсчет всех товаров в корзине.
#         """
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         """
#         Подсчет стоимости товаров в корзине.
#         """
#         return sum(Decimal(item['price']) * item['quantity'] for item in
#                    self.cart.values())