from django.shortcuts import render
from rest_framework import viewsets
from todoapp import models 
from todoapp import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    authentication_classes = (TokenAuthentication,)
    serializer_class  = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
   


class UserTodoListViewSet(viewsets.ModelViewSet):
    """Handles creaing, reading and updating profile feeds items"""
    serializer_class = serializers.UserTodoItemsSerializers
    queryset = models.UserTodoList.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)




class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

   
