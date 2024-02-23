from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'airport', views.AirportViewSet)
router.register(r'airline', views.AirlineViewSet)
router.register(r'runway', views.RunwayViewSet)
router.register(r'flight', views.FlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
