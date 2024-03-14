from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'image',
            'phone_number',
            'height',
            'weight',
            'blood_gr',
            'age'
        )
