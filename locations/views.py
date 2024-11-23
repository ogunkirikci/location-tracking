from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LocationData
from .serializers import LocationDataSerializer
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
import logging
from prometheus_client import Counter, Histogram
import time
from django.core.cache import cache
from django.conf import settings
from django.views.decorators.cache import cache_page

logger = logging.getLogger(__name__)

# Metrics
REQUEST_COUNTER = Counter(
    'location_api_requests_total',
    'Number of requests to location API endpoints',
    ['endpoint']
)

RESPONSE_TIME = Histogram(
    'location_api_response_time_seconds',
    'Response time for location API endpoints',
    ['endpoint']
)

REQUEST_COUNT = Counter(
    'django_http_requests_total_by_method',
    'HTTP requests total by method',
    ['method']
)

RESPONSE_TIME = Histogram(
    'django_http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

# Metric definitions
REQUEST_LATENCY = Histogram(
    'django_http_requests_latency_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

REQUEST_COUNT = Counter(
    'django_http_requests_total',
    'Total requests by method',
    ['method']
)

class LocationDataViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LocationData.objects.all()
    serializer_class = LocationDataSerializer

    @method_decorator(cache_page(settings.CACHE_TTL))
    @REQUEST_LATENCY.labels(method='GET', endpoint='locations-list').time()
    def list(self, request, *args, **kwargs):
        REQUEST_COUNT.labels(method='GET').inc()
        start_time = time.time()
        response = super().list(request, *args, **kwargs)
        RESPONSE_TIME.labels(
            method='GET',
            endpoint='locations-list'
        ).observe(time.time() - start_time)
        return response

    @method_decorator(cache_page(settings.CACHE_TTL))
    @action(detail=False, methods=['GET'])
    def latest(self, request):
        device_id = request.query_params.get('device_id')
        if not device_id:
            return Response({'error': 'device_id is required'}, status=400)
            
        cache_key = f'latest_location_{device_id}'
        result = cache.get(cache_key)
        
        if result is None:
            queryset = self.get_queryset().filter(device_id=device_id)
            if not queryset.exists():
                return Response({'error': 'No data found'}, status=404)
                
            latest = queryset.latest('timestamp')
            serializer = self.get_serializer(latest)
            result = serializer.data
            cache.set(cache_key, result, settings.CACHE_TTL)
        
        return Response(result)

    @action(detail=False, methods=['GET'])
    def date_range(self, request):
        start_time = time.time()
        REQUEST_COUNTER.labels(endpoint='date_range').inc()
        
        try:
            device_id = request.query_params.get('device_id')
            logger.info(f"Date range request for device: {device_id}")
            return super().date_range(request)
        finally:
            RESPONSE_TIME.labels(endpoint='date_range').observe(
                time.time() - start_time
            )

    @REQUEST_LATENCY.labels(method='POST', endpoint='locations-create').time()
    def create(self, request, *args, **kwargs):
        REQUEST_COUNT.labels(method='POST').inc()
        return super().create(request, *args, **kwargs)
