from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .permissions import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# RegionAPIView

class RegionAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            region = get_object_or_404(Region, pk=pk)
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

        region = get_object_or_404(Region, pk=pk)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        region = get_object_or_404(Region, pk=pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RegionalEmployeeAPIView

class RegionalEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            regional_employee = get_object_or_404(RegionalEmployee, pk=pk)
            serializer = RegionSerializer(regional_employee)
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

        regional_employee = get_object_or_404(RegionalEmployee, pk=pk)
        serializer = RegionSerializer(regional_employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        regional_employee = get_object_or_404(RegionalEmployee, pk=pk)
        regional_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TouristAPIView

class TouristAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None):
        if pk is not None:
            tourist = get_object_or_404(Tourist, pk=pk)
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

        tourist = get_object_or_404(Tourist, pk=pk)
        # Check if the user is a CentralEmployee or the tourist themselves
        if not IsCentralEmployee().has_permission(request, self) and request.user.id != tourist.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TouristSerializer(tourist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tourist = get_object_or_404(Tourist, pk=pk)
        tourist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CityAPIView

class CityAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = City.objects.all()
        region_id = self.request.query_params.get('region_id')

        if region_id:
            queryset = queryset.filter(region=region_id)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('region_id', openapi.IN_QUERY, description='region_id', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            city = get_object_or_404(City, pk=pk)
            serializer = CitySerializer(city)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, view, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, view, serializer.data)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, view, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# EventAPIView
class EventAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = EventAPIView.objects.all()
        city_id = self.request.query_params.get('city_id')

        if city_id:
            queryset = queryset.filter(city=city_id)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('city_id', openapi.IN_QUERY, description='city_id', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            event = get_object_or_404(Event, pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        event = get_object_or_404(Event, pk=pk)
        city = event.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CategoryAPIView

class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            category = get_object_or_404(Category, pk=pk)
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

        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ThemeAPIView

class ThemeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            theme = get_object_or_404(Theme, pk=pk)
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

        theme = get_object_or_404(Theme, pk=pk)
        serializer = ThemeSerializer(theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        theme = get_object_or_404(Theme, pk=pk)
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TransportationAPIView

class TransportationAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            transportation = get_object_or_404(Transportation, pk=pk)
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

        transportation = get_object_or_404(Transportation, pk=pk)
        serializer = TransportationSerializer(
            transportation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        transportation = get_object_or_404(Transportation, pk=pk)
        transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CommentAPIView

class CommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Comment.objects.all()
        tourist_id = self.request.query_params.get('tourist_id')

        if tourist_id:
            queryset = queryset.filter(tourist=tourist_id)

        return queryset
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('tourist_id', openapi.IN_QUERY, description='tourist_id', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            if not IsTourist().has_permission(request, view):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            if not IsTourist().has_permission(request, view, comment):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if not (IsCentralEmployee().has_permission(request, self) or 
                IsTourist().has_permission(request, view, comment)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterestAPIView

class PointOfInterestAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = PointOfInterest.objects.all()

        # Search in name and description
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # filters (category, theme, city)
        category_filter = self.request.query_params.get('category')
        theme_filter = self.request.query_params.get('theme')
        city_filter = self.request.query_params.get('city')

        if category_filter:
            queryset = queryset.filter(category__name__icontains=category_filter)

        if theme_filter:
            queryset = queryset.filter(theme__name__icontains=theme_filter)

        if city_filter:
            queryset = queryset.filter(city__name__icontains=city_filter)
            
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description='search', type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, description='category', type=openapi.TYPE_INTEGER),
            openapi.Parameter('theme', openapi.IN_QUERY, description='theme', type=openapi.TYPE_INTEGER),
            openapi.Parameter('city', openapi.IN_QUERY, description='city', type=openapi.TYPE_INTEGER),

        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            point_of_interest = get_object_or_404(PointOfInterest, pk=pk)
            serializer = PointOfInterestSerializer(point_of_interest)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = self.get_queryset()
        serializer = PointOfInterestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PointOfInterestSerializer(data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        poi = get_object_or_404(PointOfInterest, pk=pk)
        serializer = PointOfInterestSerializer(poi, data=request.data)
        if serializer.is_valid():
            city = serializer.validated_data.get('city')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poi = get_object_or_404(PointOfInterest, pk=pk)
        city = poi.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        poi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PointOfInterest_TransportationAPIView

class PointOfInterest_TransportationAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = PointOfInterest_Transportation.objects.all()
        point_of_interest_id = self.request.query_params.get('point_of_interest_id')

        if point_of_interest_id:
            queryset = queryset.filter(point_of_interest=point_of_interest_id)

        return queryset
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest_id', openapi.IN_QUERY, description='point_of_interest_id', type=openapi.TYPE_INTEGER),

        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            poi_transportation = get_object_or_404(PointOfInterest_Transportation, pk=pk)
            serializer = PointOfInterest_TransportationSerializer(poi_transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        serializer = PointOfInterestTransportationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PointOfInterest_TransportationSerializer(
            data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = get_object_or_404(PointOfInterest_Transportation, pk=pk)
        serializer = PointOfInterest_TransportationSerializer(
            poi_transportation, data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = get_object_or_404(PointOfInterest_Transportation, pk=pk)
        point_of_interest = poi_transportation.point_of_interest
        city = point_of_interest.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# OpeningHoursAPIView

class OpeningHoursAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = OpeningHours.objects.all()
        point_of_interest_id = self.request.query_params.get('point_of_interest_id')

        if point_of_interest_id:
            queryset = queryset.filter(point_of_interest=point_of_interest_id)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest_id', openapi.IN_QUERY, description='point_of_interest_id', type=openapi.TYPE_INTEGER),

        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            opening_hours = get_object_or_404(OpeningHours, pk=pk)
            serializer = OpeningHoursSerializer(opening_hours)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = OpeningHoursSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OpeningHoursSerializer(data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        opening_hours = get_object_or_404(OpeningHours, pk=pk)
        serializer = OpeningHoursSerializer(opening_hours, data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        opening_hours = get_object_or_404(OpeningHours, pk=pk)
        point_of_interest = opening_hours.point_of_interest
        city = point_of_interest.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        opening_hours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PhotoAPIView

class PhotoAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Photo.objects.all()
        point_of_interest_id = self.request.query_params.get('point_of_interest_id')

        if point_of_interest_id:
            queryset = queryset.filter(point_of_interest=point_of_interest_id)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest_id', openapi.IN_QUERY, description='point_of_interest_id', type=openapi.TYPE_INTEGER),

        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            photo = get_object_or_404(Photo, pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)
        point_of_interest = photo.point_of_interest
        city = point_of_interest.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)

        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VideoAPIView

class VideoAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Video.objects.all()
        point_of_interest_id = self.request.query_params.get('point_of_interest_id')

        if point_of_interest_id:
            queryset = queryset.filter(point_of_interest=point_of_interest_id)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest_id', openapi.IN_QUERY, description='point_of_interest_id', type=openapi.TYPE_INTEGER),

        ]
    )
    def get(self, request, pk=None):
        if pk is not None:
            video = get_object_or_404(Video, pk=pk)
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        video = get_object_or_404(Video, pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            city = point_of_interest.city
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = get_object_or_404(Video, pk=pk)
        point_of_interest = video.point_of_interest
        city = point_of_interest.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)

        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)