from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from rest_framework import exceptions


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    Email=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        Email=data.get("Email","")
        password=data.get("password","")
        if Email and password:
            user=authenticate(Email=Email,password=password)
            if user:
                data["user"]=user
            else:
                raise exceptions.ValidationError("Invalid credentials")
        else:
            raise exceptions.ValidationError("Must enter both Email and password")
        return data