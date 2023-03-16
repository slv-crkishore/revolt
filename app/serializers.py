from rest_framework import serializers
from app.models import UserModel, School, Classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if 'username' not in validated_data:
            raise serializers.ValidationError("Username is required")
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, validated_data):
        data = super().validate(validated_data)

        refresh = self.get_token(self.user)
        breakpoint()
        data["access"] = str(refresh.access_token)
        del data["refresh"]
        return data


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
