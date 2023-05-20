from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SiyahaDZ API",
        default_version='v1',
        description="API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('regions/', RegionAPIView.as_view(), name='regions'),
    path('regions/<int:pk>/', RegionAPIView.as_view(), name='region-detail'),
    path('cities/', CityAPIView.as_view(), name='cities'),
    path('cities/<int:pk>/', CityAPIView.as_view(), name='city-detail'),
    path('events/', EventAPIView.as_view(), name='events'),
    path('events/<int:pk>/', EventAPIView.as_view(), name='event-detail'),
    path('tourists/', TouristAPIView.as_view(), name='tourists'),
    path('tourists/<int:pk>/', TouristAPIView.as_view(), name='tourist-detail'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentAPIView.as_view(), name='comment-detail'),
    path('points-of-interest/', PointOfInterestAPIView.as_view(), name='points-of-interest'),
    path('points-of-interest/<int:pk>/', PointOfInterestAPIView.as_view(), name='point-of-interest-detail'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('themes/<int:pk>/', ThemeAPIView.as_view(), name='theme-detail'),
    path('opening-hours/', OpeningHoursAPIView.as_view(), name='opening-hours'),
    path('opening-hours/<int:pk>/', OpeningHoursAPIView.as_view(), name='opening-hours-detail'),
    path('transportations/', TransportationAPIView.as_view(), name='transportations'),
    path('transportations/<int:pk>/', TransportationAPIView.as_view(), name='transportation-detail'),
    path('point-of-interest-transportations/', PointOfInterest_TransportationAPIView.as_view(), name='point-of-interest-transportations'),
    path('point-of-interest-transportations/<int:pk>/', PointOfInterest_TransportationAPIView.as_view(), name='point-of-interest-transportation-detail'),
    path('photos/', PhotoAPIView.as_view(), name='photos'),
    path('photos/<int:pk>/', PhotoAPIView.as_view(), name='photo-detail'),
    path('videos/', VideoAPIView.as_view(), name='videos'),
    path('videos/<int:pk>/', VideoAPIView.as_view(), name='video-detail'),
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
