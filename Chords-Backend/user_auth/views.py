from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from user_auth.models import Token, User
from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
import uuid
from pyfcm import FCMNotification
import traceback
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from user_auth.serializers import PasswordResetSerializer, TokensSerializer, UserLoginSerializers, UserRegistrationSerializer

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_key = get_tokens_for_user(user)['access']

            token_data = {
                "key": token_key,
                "user": user.id
            }

            token_serializer = TokensSerializer(data=token_data)
            if token_serializer.is_valid():
                token_serializer.save()

            return Response({
                'status': True, 
                'status_code': 200, 
                'message': 'Registration Successful', 
                'data': {
                    'user': serializer.data,
                    'token': token_key,
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': False, 
            'status_code': 400, 
            'message': 'Email already exists',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                key = get_tokens_for_user(user)

                token_data = {
                    "key": key["access"],
                    "user": user.id
                }

                token_serializer = TokensSerializer(data=token_data)
                if token_serializer.is_valid():
                    token_serializer.save()

                profile_serializer = UserRegistrationSerializer(user)

                return Response({
                    'status': True,
                    'status_code': 200,
                    'message': 'SignIn Success',
                    'data': {
                        'user': {
                            'name': user.name,
                            'email': user.email,
                            'phone': user.phone,
                        },
                        
                        'profile': profile_serializer.data,
                        'token': key
                    }
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    'status': False,
                    'status_code': 400,
                    'message': 'Invalid Credentials, Please try again',
                    'data': None
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'status_code': 400,
                'message': 'Invalid data',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PasswordResetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
