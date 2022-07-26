from pyexpat import model
from rest_framework import serializers
from .models import CustomUser, User_Profile, Address_Global
from drf_writable_nested import WritableNestedModelSerializer

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'created_at', 'updated_at')

class Address_GlobalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address_Global
        fields = "__all__"

class User_ProfileSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = CustomUserSerializer()
    address_info = Address_GlobalSerializer()

    class Meta:
        model = User_Profile
        fields = '__all__'

