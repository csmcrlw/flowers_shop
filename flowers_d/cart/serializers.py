from .models import User, Cart
from rest_framework import serializers

class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже есть')
        return value

class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем не найден')
        return value

    def validate(self, attrs):
        user = User.objects.get(username=attrs['username'])
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError({'password': 'Неверный пароль'})
        return attrs

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'quantity']

class UserSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'phone', 'email', 'cart']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'created_at', 'updated_at']
#
