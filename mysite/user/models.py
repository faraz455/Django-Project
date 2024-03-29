from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomeUserManager(BaseUserManager):
    # funtion that create users and email is neccesary
    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        # User created
        user = self.model(email=email, **extra_fields)
        # Password hashing
        user.set_password(password)
        # User gets saved
        user.save()
        return user

    # Function that create super user with some mendatory default fields
    # After neccesary checks it calls _create_user function
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', "admin")

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super user must have is_staff equal to True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super user must have is_superuser equal to True")

        return self._create_user(email, password, **extra_fields)

# Class used to create custom user with objec having custome user manager
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # field required for a user
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = CustomeUserManager() 

    def __str__(self) :
        return self.email

class Address_Global(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class User_Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='user_profile', on_delete=models.CASCADE
        )
    address_info = models.ForeignKey(
        Address_Global, related_name="user_address", null=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField(upload_to = 'profile_pics')
    dob = models.DateField()

    def __str__(self):
        return self.user.email
