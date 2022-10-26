from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from bflowers.models import Product
from .models import User, Cart, CustomUser
from .permissions import IsOwnerOrReadOnly
from .serializers import CartSerializer, LoginUser, RegisterUser, UserAdminSerializer
import pyttsx3

class RegisterUser(GenericAPIView):
    queryset = User
    serializer_class = RegisterUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)

class LoginUser(GenericAPIView):
    queryset = User
    serializer_class = LoginUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = Token.objects.get(user__username=serializer.validated_data['username'])
        return Response({'token': token.key})

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, is_ordered=True)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        super().perform_create(serializer)

    @action(detail=True, methods=['get'])
    def index(self, request, pk):
        cart = Cart.objects.filter(user=self.request.user).values_list('products')
        products = []
        for c in cart:
            for c1 in c:
                product = str(Product.objects.get(pk=c1))
                products.append(product)
        obj = ', '.join(products)
        engine = pyttsx3.init()
        engine.say(f'Ваш заказ: {obj}')
        engine.runAndWait()
        return Response()


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = (IsAdminUser, )






