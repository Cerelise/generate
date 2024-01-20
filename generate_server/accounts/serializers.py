from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    # 验证邮箱是否存在
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("该邮箱已被使用！")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        # 将用户的密码使用哈希算法处理
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","avatar","username","is_vip","phone","description")

    def to_representation(self, value):
        data = super().to_representation(value)
        if data['avatar']:
            data['avatar'] = 'http://127.0.0.1:8000' + data['avatar']
        else:
            data['avatar'] = 'http://127.0.0.1:8000/media/avatarDefault.png'
        return data