from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ["email","password"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

class CurrentUserPicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","email"]
