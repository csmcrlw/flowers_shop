# Generated by Django 4.1.2 on 2022-10-25 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_cart_item_remove_cart_quantity_cartproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproducts',
            old_name='item',
            new_name='products',
        ),
    ]
