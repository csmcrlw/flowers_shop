from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, default='')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)    # остатки продукта
    available = models.BooleanField(default=True)
    # created = models.DateTimeField('Создано', auto_now_add=True, db_index=True)
    # updated = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def is_available(self):
        if self.stock == 0:
            self.available = False
        return self.available

