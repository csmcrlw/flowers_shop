from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='products')
    name = models.CharField('Название', max_length=255, unique=True)
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
