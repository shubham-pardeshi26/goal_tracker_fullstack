# serializers.py
from rest_framework import serializers
from .models import Goal_Users
import bcrypt


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal_Users
        fields = ("first_name", "last_name", "mobile", "password", "email", "country")

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        validated_data["password"] = hashed_password.decode("utf-8")
        user = Goal_Users.objects.create(**validated_data)
        return user
