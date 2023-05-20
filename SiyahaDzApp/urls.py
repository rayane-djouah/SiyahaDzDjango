from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
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

router = routers.DefaultRouter()
router.register(r'regions', RegionAPIView, basename='region')
router.register(r'cities', CityAPIView, basename='city')
router.register(r'events', EventAPIView, basename='event')
router.register(r'tourists', TouristAPIView, basename='tourist')
router.register(r'regionalemployees', RegionalEmployeeAPIView, basename='regional-employee')
router.register(r'centralemployees', CentralEmployeeAPIView, basename='central-employee')
router.register(r'comments', CommentAPIView, basename='comment')
router.register(r'points-of-interest', PointOfInterestAPIView, basename='point-of-interest')
router.register(r'categories', CategoryAPIView, basename='category')
router.register(r'themes', ThemeAPIView, basename='theme')
router.register(r'opening-hours', OpeningHoursAPIView, basename='opening-hours')
router.register(r'transportations', TransportationAPIView, basename='transportation')
router.register(r'point-of-interest-transportations', PointOfInterest_TransportationAPIView, basename='point-of-interest-transportation')
router.register(r'photos', PhotoAPIView, basename='photo')
router.register(r'videos', VideoAPIView, basename='video')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
