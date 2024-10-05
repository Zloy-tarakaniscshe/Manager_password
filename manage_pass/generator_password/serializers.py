from rest_framework import serializers

from generator_password.models import Password


class PasswordSerializer(serializers.Serializer):
    class Meta:
        model = Password
        fields = ['service_name', 'password']
