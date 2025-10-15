from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=30)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    email = serializers.EmailField(required=True, max_length=254)
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=50)
    password_check = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_check']

    def validate(self, data):
        if data.get('password') != data.get('password_check'):
            raise serializers.ValidationError({"Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_check')
        return User.objects.create_user(**validated_data)
