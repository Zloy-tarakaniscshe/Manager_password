from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Password
from generator_password.gen_pass.encryption import generate_encrypt_password


class PasswordView(APIView):
    def get(self, request, service_name):
        try:
            password_entry = Password.objects.get(service_name=service_name)
            return Response(
                {
                    "service_name": password_entry.service_name,
                    "password": password_entry.encrypted_password
                },
                status=status.HTTP_200_OK
            )
        except Password.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, service_name):

        password = generate_encrypt_password()
        try:
            password_entry = Password.objects.get(service_name=service_name)
            password_entry.encrypted_password = password
            password_entry.save()
        except Password.DoesNotExist:
            password_entry = Password.objects.create(service_name=service_name, encrypted_password=password)
            password_entry.save()
        return Response({"password": password}, status=status.HTTP_201_CREATED)


class PasswordSearchView(APIView):
    def get(self, request):
        part_of_service_name = request.query_params.get('service_name')
        try:
            query = Password.objects.filter(service_name__icontains=part_of_service_name)
            return Response(query.values(), status=status.HTTP_200_OK)
        except Password.DoesNotExist:
            return Response({"error": "No service name provided."}, status=status.HTTP_400_BAD_REQUEST)


def page_not_found(request, exception):
    return Response({"error": "No service name provided."}, status=status.HTTP_404_NOT_FOUND)
