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
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),    path('regions/', RegionAPIView.as_view(), name='regions'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('regions/<str:pk>/', RegionAPIView.as_view(), name='region-detail'),
    path('cities/', CityAPIView.as_view(), name='cities'),
    path('cities/<str:pk>/', CityAPIView.as_view(), name='city-detail'),
    path('events/', EventAPIView.as_view(), name='events'),
    path('events/<str:pk>/', EventAPIView.as_view(), name='event-detail'),
    path('regional-employees/', RegionalEmployeeAPIView.as_view(), name='regional-employees'),
    path('regional-employees/<str:pk>/', RegionalEmployeeAPIView.as_view(), name='regional-employee-detail'),
    path('tourists/', TouristAPIView.as_view(), name='tourists'),
    path('tourists/<str:pk>/', TouristAPIView.as_view(), name='tourist-detail'),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<str:pk>/', CommentAPIView.as_view(), name='comment-detail'),
    path('points-of-interest/', PointOfInterestAPIView.as_view(), name='points-of-interest'),
    path('points-of-interest/<str:pk>/', PointOfInterestAPIView.as_view(), name='point-of-interest-detail'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<str:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('themes/<str:pk>/', ThemeAPIView.as_view(), name='theme-detail'),
    path('opening-hours/', OpeningHoursAPIView.as_view(), name='opening-hours'),
    path('opening-hours/<str:pk>/', OpeningHoursAPIView.as_view(), name='opening-hours-detail'),
    path('transportations/', TransportationAPIView.as_view(), name='transportations'),
    path('transportations/<str:pk>/', TransportationAPIView.as_view(), name='transportation-detail'),
    path('point-of-interest-transportations/', PointOfInterest_TransportationAPIView.as_view(), name='point-of-interest-transportations'),
    path('point-of-interest-transportations/<str:pk>/', PointOfInterest_TransportationAPIView.as_view(), name='point-of-interest-transportation-detail'),
    path('photos/', PhotoAPIView.as_view(), name='photos'),
    path('photos/<str:pk>/', PhotoAPIView.as_view(), name='photo-detail'),
    path('videos/', VideoAPIView.as_view(), name='videos'),
    path('videos/<str:pk>/', VideoAPIView.as_view(), name='video-detail'),
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
