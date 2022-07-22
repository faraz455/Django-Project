import jwt
from .models import Jwt
from user.models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from .serializer import LoginSerializer, RegisterSerializer, RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import Authentication

# Get random data for refresh token
def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase +string.digits,k =length))

# Token that need to be provide by user to server
def get_access_token(payload):
    return jwt.encode(
        # expiration is set 5 minutes so that user cant access server for long time
        {"exp": datetime.now()+ timedelta(minutes = 5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

# Token that is issued by server to the user 
def get_refresh_token():
    return jwt.encode(
        # expiration time set to an year so it remain login till user logouts
        {"exp": datetime.now()+timedelta(days=365),"data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

# Login view created to login the registered user
class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
        # valids the data
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception = True)

        # check if the user name and password matches the existing user data
        user = authenticate(
            username = serializer.validated_data['email'], 
            password = serializer.validated_data['password']
            )
        # incase user doesnt exist
        if not user:
            return Response({"Error": " Invalid Email or password"}, status="400")
        Jwt.objects.filter(user_id = user.id).delete()
        # access and refresh token created
        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()
        # Jwt class object created
        Jwt.objects.create(
            user_id = user.id , access = access.decode(), refresh = refresh.decode()
        )
        return Response({"access": access, "refresh" : refresh})

# Register view created to register the new user 
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception = True)
          
        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({"success": "user created."})

# Refresh view created to refresh the token
class RefreshView(APIView):
    serializer_class = RefreshSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True)
        # gets the object
        try:
            active_jwt = Jwt.objects.get(
                refresh= serializer.validated_data["refresh"]
                )
        except Jwt.DoesNotExist:
            return Response({"error":"Refresh token not found"}, status="400")
        # Response whether token expired or not
        if not Authentication.varify_token(serializer.validated_data["refresh"]):
            return Response({"error": "Token is invalid or expired"})
        # Gets the access and refresh token
        access = get_access_token({"user_id": active_jwt.user.id})
        refresh = get_refresh_token()
        # Assign the access and refresh token
        active_jwt.access = access.decode()
        active_jwt.refresh = refresh.decode()
        active_jwt.save()

        return Response({"access": access, "refresh" : refresh})


# login user sercure info
class GetSecureInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print("User name:", request.user)
        return Response({"data": "This is sercure infomation"})
