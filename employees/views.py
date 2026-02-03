from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

from employees.serializers import UserSerializer



class UserSignUpView(APIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = self.serializer_class(data=data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


