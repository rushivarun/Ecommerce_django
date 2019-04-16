from django.shortcuts import render

from django.shortcuts import render
from . import models
from . import serializer
from rest_framework import generics
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.


class SignupView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.SignupSerializer
    permission_classes = (AllowAny,)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request,):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
