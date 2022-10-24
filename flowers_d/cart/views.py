from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Cart
from .serializers import UserSerializer, CartSerializer
from bflowers.models import Product


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

    @action(detail=True, methods=['post', 'put', 'patch'])
    def add_to_cart(request, product_id, quantity):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(product, product.price, quantity)

    @action(detail=True, methods=['delete'])
    def remove_from_cart(request, product_id):
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.remove(product)



    # @action(methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
    # def checkout(self, request, *args, **kwargs):
    #
    #     try:
    #         user = User.objects.get(pk=int(kwargs.get('userId')))
    #     except Exception as e:
    #         return Response(status=status.HTTP_404_NOT_FOUND,
    #                         data={'Error': str(e)})
    #
    #     cart_helper = CartHelper(user)
    #     checkout_details = cart_helper.prepare_cart_for_checkout()
    #
    #     if not checkout_details:
    #         return Response(status=status.HTTP_404_NOT_FOUND,
    #                         data={'error': 'Cart of user is empty.'})
    #
    #     return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})



# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
# from bflowers.models import Product
# from .cart import Cart
# from .forms import CartAddProductForm
#
#
# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/detail.html', {'cart': cart})
#


# class CartViewSet(ModelViewSet):
#     serializer_class = serializers.Cart
#
#     @action(detail=True, methods=['post', 'put', 'patch'])
#     def add_to_cart(request, product_id, quantity):
#         product = Product.objects.get(id=product_id)
#         cart = Cart(request)
#         cart.add(product, product.price, quantity)
#
#     @action(detail=True, methods=['delete'])
#     def remove_from_cart(request, product_id):
#         product = Product.objects.get(id=product_id)
#         cart = Cart(request)
#         cart.remove(product)
#
#     def get_queryset(self):
#         serializer = serializers.Cart()
#         return Response(serializer.data)
