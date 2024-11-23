from django.contrib.postgres.indexes import BrinIndex
from django.db import models


class LocationData(models.Model):
    device_id = models.CharField(max_length=100, db_index=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["device_id", "-timestamp"]),
            models.Index(fields=["-timestamp"]),
        ]
        # Composite index for location queries
        index_together = [
            ["device_id", "timestamp", "latitude", "longitude"],
        ]

    def __str__(self):
        return f"Device {self.device_id} at ({self.latitude}, {self.longitude})"
