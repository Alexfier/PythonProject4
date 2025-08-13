from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from users.models import User
from users.serliazers import UserSerializer


# Create your views here.

class UserCreteAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserList(generics.ListCreateAPIView):
    # Описываем класс-контроллер на основе базового класса дженерика и указываем необходимые атрибуты
    queryset = User.objects.all()
    serializer_class = UserSerializer
