from rest_framework import serializers
from .models import CustomUser, User_Profile, Address_Global
from drf_writable_nested import WritableNestedModelSerializer

class Address_GlobalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address_Global
        fields = "__all__"

class User_ProfileSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address_info = Address_GlobalSerializer()

    class Meta:
        model = User_Profile
        fields = "__all__"

class CustomUserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user_profile = User_ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ("email", "name", "user_profile", "created_at", "updated_at")