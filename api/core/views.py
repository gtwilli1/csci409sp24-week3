from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Airport
from .serializers import AirportSerializer
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

from rest_framework import viewsets
from .models import Airline
from .serializers import AirlineSerializer
class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

from rest_framework import viewsets
from .models import Runway
from .serializers import RunwaySerializer
class RunwayViewSet(viewsets.ModelViewSet):
    queryset = Runway.objects.all()
    serializer_class = RunwaySerializer


from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
