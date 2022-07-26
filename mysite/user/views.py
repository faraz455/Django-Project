from rest_framework.viewsets import ModelViewSet
from .serializer import CustomUserSerializer, User_ProfileSerializer,Address_GlobalSerializer, CustomUser, User_Profile, Address_Global

class CustomeUserView(ModelViewSet):
    # CustomUser had a indirect relationship with profile so we can use prefetch_related using the related_name
    # we have used user_profile__address_info for the address_info as it is inside the user_profile
    queryset= CustomUser.objects.prefetch_related(
        'user_profile', 'user_profile__address_info')
    serializer_class = CustomUserSerializer

# if the model has direct relation than we can use select_related query 
# if the model has indirect relation than we can use prefetch_related query using related_name used

class User_ProfileView(ModelViewSet):
    # user_profile had a direct relationship with address so we can use select_related with address_info
    queryset = User_Profile.objects.select_related("address_info")
    serializer_class = User_ProfileSerializer

# Queries such as prefetch_related and select_related are used to less sql statements and increase speed

## class Address_GlobalView(ModelViewSet):
##     queryset = Address_Global.objects.all()
##     serializer_class = Address_GlobalSerializer

