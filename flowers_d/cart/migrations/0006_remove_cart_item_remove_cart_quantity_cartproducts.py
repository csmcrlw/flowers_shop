# Generated by Django 4.1.2 on 2022-10-25 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bflowers', '0003_alter_category_options_alter_product_options'),
        ('cart', '0005_user_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('item', models.ManyToManyField(blank=True, null=True, related_name='cart_products', to='bflowers.product')),
            ],
        ),
    ]
