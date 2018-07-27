# This imports all available serializer types available in Django REST Framework.
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    # There is a good pre-defined validation. For example here if we'll provide a name longer than 10 characters,
    # the error message will occur.
    name = serializers.CharField(max_length=10)
