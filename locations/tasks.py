from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone

@shared_task
def process_location_data(location_id):
    from .models import Location
    location = Location.objects.get(id=location_id)
    # İşlem mantığı
    return f"Location {location_id} processed" 