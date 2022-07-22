from rest_framework.viewsets import ModelViewSet
from .serializer import UserProfileSerializer, CustomUserSerializer, UserProfile, CustomUser

class CustomeUserView(ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
