from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField,
    StringRelatedField, PrimaryKeyRelatedField
)
from .models import UserProfile, HomeDetails, HomeRentDetails, HomeRentDetails
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email'
        ]


class ProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = [
            'user', 'phone', 'address'
        ]
    def update(self, instance, validated_data):
        print('.......', validated_data)
        return validated_data


class HomeDetailSerializer(ModelSerializer):
    class Meta:
        model = HomeDetails
        fields = [
            'rent', 'title', 'description', 'image'
        ]


class HomeRentSerializer(ModelSerializer):
    class Meta:
        model = HomeRentDetails
        fields = [
            'home', 'renter', 'start_date',
            'end_date', 'description'
        ]

