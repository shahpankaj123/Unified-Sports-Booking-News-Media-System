import uuid
import random

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone

import datetime

class UserTypes(models.Model):

    class Meta:
        db_table = 'UserTypes'

    UserTypeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserType = models.CharField(max_length=50)

    def userTypeId(self): return self.UserTypeID
    def userType(self): return self.UserType

    def __str__(self):
        return self.UserType


class UserManager(BaseUserManager):
    def create_superuser(self, Email ,FirstName, LastName, UserName, password , PhoneNumber,  **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('IsActive', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username = UserName, email = Email, password = password, first_name = FirstName, last_name= LastName, phone_number=PhoneNumber, user_type = UserTypes.objects.get(UserType = 'Admin'), **other_fields )

    def create_user(self, username, email, password, first_name, last_name, user_type,phone_number, **other_fields):
        if not email:
            raise ValueError('Users must have an email daddress.')

        email = self.normalize_email(email)
        user = self.model(Email = email, FirstName = first_name, LastName = last_name, UserName = username, UserType = user_type , PhoneNumber = phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user    

class Users(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'Users'

    UserID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserType = models.ForeignKey(UserTypes, on_delete=models.CASCADE,db_column='UserType')
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=50, default='')
    ProfileImage = models.CharField(max_length=300, default='')
    Email = models.EmailField(max_length=200, unique=True, editable=True)
    UserName = models.CharField(max_length=100, unique=True)
    PhoneNumber = models.CharField(max_length=15, null=True)
    StartDate = models.DateTimeField(default=timezone.now)
    LastLogin = models.DateTimeField(auto_now=True)
    LastLogout = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    LoginTry = models.IntegerField(null=True, default=0)
    LoginStatus = models.CharField(max_length=40 , default='')


    objects = UserManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['FirstName','LastName','UserName','PhoneNumber']

    def __str__(self):
        return self.Email 

class Status(models.Model):
    class Meta:
        db_table = "Status"

    StatusID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.Status

class City(models.Model):
    class Meta:
        db_table = "City"

    CityID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CityName = models.CharField(max_length=50)

    def __str__(self):
        return self.CityName

class Gender(models.Model):
    class Meta:
        db_table = 'Gender'

    GenderID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Gender = models.CharField(max_length=25)

    def __str__(self):
        return self.Gender

class PaymentType(models.Model):
    class Meta:
        db_table = "PaymentType"

    PaymentTypeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PaymentTypeName = models.CharField(max_length=50) 

    def __str__(self):
        return self.PaymentTypeName

class OTPData(models.Model):
    class Meta:
        db_table = "OTPData"

    OTPDataID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    OTP = models.CharField(max_length = 6, null = False)
    OTPUser = models.ForeignKey(Users,on_delete=models.SET_NULL, null=True)
    IsValid = models.BooleanField(default = True)
    ValidDateTill = models.DateField()
    ValidTimeTill = models.TimeField() 

    def __str__(self):
        return self.OTPUser.Email + self.OTP

class ErrorMessages(models.Model):
    class Meta:
        db_table = 'ErrorMessages'

    ErrorMessageID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ErrorTitle = models.CharField(max_length=100)
    ErrorLogs = models.TextField()
    User = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, db_column='UserID')
    Status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, db_column='StatusID')
    CreatedAt = models.DateTimeField(default=datetime.datetime.now)
    UpdatedAt = models.DateTimeField(auto_now_add=True, null=True) 

class SportCategory(models.Model):

    class Meta:
        db_table = 'SportCategory'

    SportCategoryID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    SportCategory = models.CharField(max_length=100)

    def __str__(self):
        return self.SportCategory

            


         

