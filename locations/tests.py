import json
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import LocationData


class LocationDataModelTests(TestCase):
    def setUp(self):
        """Create test data"""
        self.location_data = LocationData.objects.create(
            device_id="test_device", latitude=41.0082, longitude=28.9784, speed=50.5
        )

    def test_location_creation(self):
        """Konum verisi oluşturma testi"""
        self.assertTrue(isinstance(self.location_data, LocationData))
        self.assertEqual(self.location_data.device_id, "test_device")
        self.assertEqual(float(self.location_data.latitude), 41.0082)
        self.assertEqual(float(self.location_data.longitude), 28.9784)
        self.assertEqual(self.location_data.speed, 50.5)

    def test_location_str_representation(self):
        """__str__ method test"""
        expected_str = f"Device test_device at ({self.location_data.latitude}, {self.location_data.longitude})"
        self.assertEqual(str(self.location_data), expected_str)


class LocationDataAPITests(APITestCase):
    def setUp(self):
        """Create test data"""
        # Create a few test data
        self.test_data = {"device_id": "test_device", "latitude": 41.0082, "longitude": 28.9784, "speed": 50.5}

        # Old date data
        self.old_location = LocationData.objects.create(
            device_id="test_device",
            latitude=41.0082,
            longitude=28.9784,
            speed=50.5,
            timestamp=timezone.now() - timedelta(days=1),
        )

        # New date data
        self.new_location = LocationData.objects.create(
            device_id="test_device", latitude=41.0083, longitude=28.9785, speed=51.5
        )

    def test_create_location(self):
        """POST /api/locations/ testi"""
        url = "/api/locations/"
        response = self.client.post(url, self.test_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data["message"], "Location data queued for processing")

    def test_get_latest_location(self):
        """GET /api/locations/latest/ testi"""
        url = "/api/locations/latest/"

        # Request without device_id
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Request with correct device_id
        response = self.client.get(f"{url}?device_id=test_device")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the latest added data is returned
        self.assertEqual(float(response.data["latitude"]), 41.0083)
        self.assertEqual(float(response.data["longitude"]), 28.9785)

    def test_get_date_range_locations(self):
        """GET /api/locations/date_range/ testi"""
        url = "/api/locations/date_range/"

        # Create a valid date range
        end_date = timezone.now()
        start_date = end_date - timedelta(days=2)

        query_params = {
            "device_id": "test_device",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
        }

        response = self.client.get(url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)

    def test_invalid_data_creation(self):
        """Invalid data sending test"""
        url = "/api/locations/"

        # Invalid latitude value
        invalid_latitude_data = {
            "device_id": "test_device",
            "latitude": 200,  # Invalid latitude
            "longitude": 28.9784,
            "speed": 50.5,
        }

        response = self.client.post(url, invalid_latitude_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("latitude", response.data.get("details", {}))

        # Invalid longitude value
        invalid_longitude_data = {
            "device_id": "test_device",
            "latitude": 41.0082,
            "longitude": -200,  # Invalid longitude
            "speed": 50.5,
        }

        response = self.client.post(url, invalid_longitude_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("longitude", response.data.get("details", {}))

        # Invalid speed value
        invalid_speed_data = {
            "device_id": "test_device",
            "latitude": 41.0082,
            "longitude": 28.9784,
            "speed": -10,  # Invalid speed
        }

        response = self.client.post(url, invalid_speed_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("speed", response.data.get("details", {}))


class LocationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.force_authenticate(user=self.user)

        self.location_data = {"latitude": 41.0082, "longitude": 28.9784, "timestamp": datetime.now().isoformat()}

    def test_create_location(self):
        response = self.client.post("/api/v1/locations/", self.location_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LocationData.objects.count(), 1)

    def test_list_locations(self):
        LocationData.objects.create(user=self.user, **self.location_data)
        response = self.client.get("/api/v1/locations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/v1/locations/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
