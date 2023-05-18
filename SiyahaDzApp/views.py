from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import *
from .serializers import *
from .permissions import *


# Region views

class RegionAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            region = Region.objects.get(pk=pk)
            serializer = RegionSerializer(region)
            return Response(serializer.data, status=status.HTTP_200_OK)
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        region = Region.objects.get(pk=pk)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        region = Region.objects.get(pk=pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# RegionalEmployee views

class RegionalEmployeeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            region = Region.objects.get(pk=pk)
            serializer = RegionSerializer(region)
            return Response(serializer.data, status=status.HTTP_200_OK)
        regional_employees = RegionalEmployee.objects.all()
        serializer = RegionalEmployeeSerializer(regional_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = RegionalEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        regional_employees = RegionalEmployee.objects.get(pk=pk)
        serializer = RegionSerializer(regional_employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        regional_employee = RegionalEmployee.objects.get(pk=pk)
        regional_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TouristAPIView

class TouristAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            tourist = Tourist.objects.get(pk=pk)
            serializer = TouristSerializer(tourist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tourists = Tourist.objects.all()
        serializer = TouristSerializer(tourists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TouristSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tourist = Tourist.objects.get(pk=pk)
        serializer = TouristSerializer(tourist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tourist = Tourist.objects.get(pk=pk)
        tourist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CityAPIView

class CityAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            city = City.objects.get(pk=pk)
            serializer = CitySerializer(city)
            return Response(serializer.data, status=status.HTTP_200_OK)
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        city = City.objects.get(pk=pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        city = City.objects.get(pk=pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# EventAPIView
class EventAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)

        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CategoryAPIView

class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ThemeAPIView

class ThemeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            theme = Theme.objects.get(pk=pk)
            serializer = ThemeSerializer(theme)
            return Response(serializer.data, status=status.HTTP_200_OK)

        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = ThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        theme = Theme.objects.get(pk=pk)
        serializer = ThemeSerializer(theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        theme = Theme.objects.get(pk=pk)
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TransportationAPIView

class TransportationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            transportation = Transportation.objects.get(pk=pk)
            serializer = TransportationSerializer(transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        transportations = Transportation.objects.all()
        serializer = TransportationSerializer(transportations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TransportationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        transportation = Transportation.objects.get(pk=pk)
        serializer = TransportationSerializer(
            transportation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        transportation = Transportation.objects.get(pk=pk)
        transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterest_TransportationAPIView
class PointOfInterest_TransportationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            point_of_interest_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
            serializer = PointOfInterest_TransportationSerializer(point_of_interest_transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        point_of_interest_transportations = PointOfInterest_Transportation.objects.all()
        serializer = PointOfInterest_TransportationSerializer(point_of_interest_transportations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PointOfInterest_TransportationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        point_of_interest_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        serializer = PointOfInterest_TransportationSerializer(point_of_interest_transportation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        point_of_interest_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        point_of_interest_transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CommentAPIView

class CommentAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterestAPIView

class PointOfInterestAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            poi = PointOfInterest.objects.get(pk=pk)
            serializer = PointOfInterestSerializer(poi)
            return Response(serializer.data, status=status.HTTP_200_OK)
        pois = PointOfInterest.objects.all()
        serializer = PointOfInterestSerializer(pois, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PointOfInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi = PointOfInterest.objects.get(pk=pk)
        serializer = PointOfInterestSerializer(poi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi = PointOfInterest.objects.get(pk=pk)
        poi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterest_TransportationAPIView

class PointOfInterest_TransportationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            poi_transportation = PointOfInterest_Transportation.objects.get(
                pk=pk)
            serializer = PointOfInterest_TransportationSerializer(
                poi_transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        poi_transportations = PointOfInterest_Transportation.objects.all()
        serializer = PointOfInterest_TransportationSerializer(
            poi_transportations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PointOfInterest_TransportationSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        serializer = PointOfInterest_TransportationSerializer(
            poi_transportation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        poi_transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# OpeningHoursAPIView

class OpeningHoursAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            opening_hours = OpeningHours.objects.get(pk=pk)
            serializer = OpeningHoursSerializer(opening_hours)
            return Response(serializer.data, status=status.HTTP_200_OK)
        opening_hours_list = OpeningHours.objects.all()
        serializer = OpeningHoursSerializer(opening_hours_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = OpeningHoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        opening_hours = OpeningHours.objects.get(pk=pk)
        serializer = OpeningHoursSerializer(opening_hours, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        opening_hours = OpeningHours.objects.get(pk=pk)
        opening_hours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterest_TransportationAPIView

class PointOfInterest_TransportationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            poi_transportation = PointOfInterest_Transportation.objects.get(
                pk=pk)
            serializer = PointOfInterest_TransportationSerializer(
                poi_transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        poi_transportations = PointOfInterest_Transportation.objects.all()
        serializer = PointOfInterest_TransportationSerializer(
            poi_transportations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PointOfInterest_TransportationSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        serializer = PointOfInterest_TransportationSerializer(
            poi_transportation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = PointOfInterest_Transportation.objects.get(pk=pk)
        poi_transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PhotoAPIView

class PhotoAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        photo = Photo.objects.get(pk=pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        photo = Photo.objects.get(pk=pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VideoAPIView

class VideoAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            video = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
