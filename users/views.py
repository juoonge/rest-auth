from django.shortcuts import render
from .api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    
