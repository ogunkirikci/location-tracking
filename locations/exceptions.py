from rest_framework.views import exception_handler
from django_ratelimit.exceptions import Ratelimited
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    if isinstance(exc, Ratelimited):
        return Response({
            'error': 'Rate limit exceeded',
            'detail': 'Too many requests. Please try again later.'
        }, status=status.HTTP_429_TOO_MANY_REQUESTS)

    response = exception_handler(exc, context)
    return response 