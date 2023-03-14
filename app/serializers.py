from rest_framework import serializers
from app.models import UserModel, School, Classes


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

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


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
