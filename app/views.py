from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from app.serializers import UserSerializer, SchoolSerializer, ClassSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from app.models import UserModel, School, Classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your views here.


class UserRegistrationView(APIView):
    http_method_names = ["post", "options"]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(ModelViewSet):
    http_method_names = ["get", "put", "patch", "delete", "options"]
    permission_classes = [IsAuthenticated]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class SchoolView(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ClassesView(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
