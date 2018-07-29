# This imports all available serializer types available in Django REST Framework.
from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    # There is a good pre-defined validation. For example here if we'll provide a name longer than 10 characters,
    # the error message will occur.
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our User Profile objects."""

    # The Meta class tells Django REST Framework what fields we wanna take
    # from our model.
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # We want to override the 'create' function in order to encrypt
    # the password.
    def create(self, validated_data):
        """Create and return a new user."""

        # Here we actually create a new user.
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])

        # Here we save the object to the database.
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for Profile Feed Items."""

    class Meta:
        model = models.ProfileFeedItem
        # ID of the object - Primary Key. User Profile - Foreign Key
        # in database.
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # We don't want to allow anyone to change 'user profile'.
        # It should be set autmatically as the ID of our logged in user (who
        # wants to add a feed item).
        extra_kwargs = {'user_profile': {'read_only': True}}
