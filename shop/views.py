from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from backend.settings import env


class EnvView(APIView):
    def post(self, request, format=None):
        password = request.data.get('password')
        print('15: password >>>', password)
        if password == env('CUSTOM_PASSWORD'):
            return JsonResponse({
                'EMAIL_HOST_PASSWORD': env('EMAIL_HOST_PASSWORD'),
                'SECRET_KEY': env('SECRET_KEY'),
                'PRODUCTION': env('PRODUCTION'),
                'FRONT_DOMAIN': env('FRONT_DOMAIN'),
                'ALLOWED_HOSTS': env('ALLOWED_HOSTS'),
                'CORS_ORIGIN_WHITELIST': env('CORS_ORIGIN_WHITELIST'),
            })
        return JsonResponse({
            'error': 'password is not correct'
        })
