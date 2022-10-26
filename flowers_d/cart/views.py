from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import User, Cart
from .permissions import IsOwnerOrReadOnly
from .serializers import CartSerializer, LoginUser, RegisterUser
from rest_framework.authtoken.models import Token


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
    permission_classes = (IsOwnerOrReadOnly, )



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser, IsOwnerOrReadOnly)




