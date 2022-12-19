from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(validators=(validate_password, ))
    password1 = serializers.CharField(validators=(validate_password, ))
    fullname = serializers.CharField()
    username = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError('The passwords do not match')
        return attrs
