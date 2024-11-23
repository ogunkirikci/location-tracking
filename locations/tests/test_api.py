from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from locations.models import Location


class LocationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.force_authenticate(user=self.user)

        self.location_data = {"latitude": 41.0082, "longitude": 28.9784, "timestamp": datetime.now().isoformat()}

    def test_create_location(self):
        response = self.client.post("/api/v1/locations/", self.location_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)

    def test_list_locations(self):
        Location.objects.create(user=self.user, **self.location_data)
        response = self.client.get("/api/v1/locations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
