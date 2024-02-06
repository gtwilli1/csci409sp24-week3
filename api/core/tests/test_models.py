"""
Tests for models.
"""

from django.test import TestCase
from core import models
from datetime import datetime

class ModelTests(TestCase):

    def test_create_airport(self):
        """Test Creating an Airport is Successful."""
        airport = models.Airport.objects.create(
            name="Myrtle Beach International",
            airport_code="MYR",
            address="1100 Jetport Rd",
            city="Myrtle Beach",
            state="SC",
            zip_code="29577"
        )
        self.assertEqual(str(airport), airport.name)

class Airline(models.Model):
    name = models.CharField(max_length=255)
    airline_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
class Runway(models.Model):
    RUNWAY_DESIGNATIONS = [
        ('L', 'Left'),
        ('C', 'Center'),
        ('R', 'Right'),
        ('N', 'None'),
    ]

    runway_number = models.IntegerField()
    runway_designation = models.CharField(max_length=1, choices=RUNWAY_DESIGNATIONS)
    length = models.IntegerField()
    width = models.IntegerField()
    airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='runways')

    def __str__(self):
        return f"{self.runway_number}{self.runway_designation}"