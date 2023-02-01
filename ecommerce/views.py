from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# class UserSerializersView(APIView):
#   def get(self, request, *args, **kwargs):
#     if request.method == 'GET':
#         users = User.objects.all()
#         # print(users,'sdsddsdsd')
#         serializer = UserSerializer(users, many=True)
       
#         return Response(serializer.data)