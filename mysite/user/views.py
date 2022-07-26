from rest_framework.viewsets import ModelViewSet
from .serializer import CustomUserSerializer, User_ProfileSerializer,Address_GlobalSerializer, CustomUser, User_Profile, Address_Global

class CustomeUserView(ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class User_ProfileView(ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer

class Address_GlobalView(ModelViewSet):
    queryset = Address_Global.objects.all()
    serializer_class = Address_GlobalSerializer