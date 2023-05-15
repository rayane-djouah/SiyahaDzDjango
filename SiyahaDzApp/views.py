from rest_framework import generics, permissions
from .models import (
    Region, City, PointOfInterest, Comment, Event,
    Category, Theme, OpeningHours, Transportation,
    PointOfInterest_Transportation, Photo, Video,
    RegionalEmployee, CentralEmployee, Tourist
)
from .serializers import (
    RegionSerializer, CitySerializer, PointOfInterestSerializer,
    CommentSerializer, EventSerializer, CategorySerializer,
    ThemeSerializer, OpeningHoursSerializer, TransportationSerializer,
    PointOfInterest_TransportationSerializer, PhotoSerializer, VideoSerializer,
    RegionalEmployeeSerializer, CentralEmployeeSerializer, TouristSerializer
)


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PointOfInterestListAPIView(generics.ListAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PointOfInterestDetailAPIView(generics.RetrieveAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class ThemeListAPIView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class ThemeDetailAPIView(generics.RetrieveAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class OpeningHoursListAPIView(generics.ListAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class OpeningHoursDetailAPIView(generics.RetrieveAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    permission_classes = [permissions.Allow


class TransportationListAPIView(generics.ListAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class TransportationDetailAPIView(generics.RetrieveAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PointOfInterestTransportationListAPIView(generics.ListAPIView):
    queryset = PointOfInterest_Transportation.objects.all()
    serializer_class = PointOfInterest_TransportationSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PointOfInterestTransportationDetailAPIView(generics.RetrieveAPIView):
    queryset = PointOfInterest_Transportation.objects.all()
    serializer_class = PointOfInterest_TransportationSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PhotoListAPIView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class PhotoDetailAPIView(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class RegionalEmployeeListAPIView(generics.ListAPIView):
    queryset = RegionalEmployee.objects.all()
    serializer_class = RegionalEmployeeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class RegionalEmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = RegionalEmployee.objects.all()
    serializer_class = RegionalEmployeeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CentralEmployeeListAPIView(generics.ListAPIView):
    queryset = CentralEmployee.objects.all()
    serializer_class = CentralEmployeeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class CentralEmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = CentralEmployee.objects.all()
    serializer_class = CentralEmployeeSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class TouristListAPIView(generics.ListAPIView):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access


class TouristDetailAPIView(generics.RetrieveAPIView):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access