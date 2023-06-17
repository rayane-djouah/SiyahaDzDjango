from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .permissions import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description='User registered successfully',
                schema=UserRegistrationSerializer,
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Invalid data or validation error',
            ),
        }
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_summary='Obtain Access and Refresh Tokens',
        operation_description='Obtains the access and refresh tokens using the provided email and password.',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),  
                'email': openapi.Schema(type=openapi.TYPE_STRING), 
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['email', 'password'],
        ),
        responses={
            200: openapi.Response(
                description='Token obtained successfully',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                    required=['access', 'refresh'],
                ),
            ),
            400: openapi.Response(
                description='Invalid credentials',
            ),
            401: openapi.Response(
                description='Unauthorized access',
            ),
        },
    )
    def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)
    
class MyTokenRefreshView(TokenRefreshView):
    """
    Customized token refresh view.
    """
    @swagger_auto_schema(
        operation_summary='Refresh Access Token',
        operation_description='Refreshes the access token using a refresh token.',
        responses={
            200: openapi.Response(
                description='Token refreshed successfully',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                    required=['access'],
                ),
            ),
            400: openapi.Response(
                description='Invalid refresh token',
            ),
            401: openapi.Response(
                description='Refresh token expired or revoked',
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserLogoutAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['refresh'],
        ),
        responses={
            status.HTTP_205_RESET_CONTENT: openapi.Response(
                description='User logged out successfully',
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Invalid data or missing refresh token',
            ),
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# RegionalEmployeeAPIView

class RegionalEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]   
    def get(self,request,pk):
        if pk is not None:
            user = User.objects.filter(email=pk)
            id = user[0].id
            regional_employee = get_object_or_404(RegionalEmployee, pk=id)
            serializer = RegionalEmployeeSerializer(regional_employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        regional_employees = RegionalEmployee.objects.all()
        serializer = RegionalEmployeeSerializer(regional_employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
            ],
        request_body=RegionalEmployeeSerializer)
    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = RegionalEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
            ],
        request_body=RegionalEmployeeSerializer)
    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        regional_employee = get_object_or_404(RegionalEmployee, pk=pk)
        serializer = RegionalEmployeeSerializer(regional_employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        regional_employee = get_object_or_404(RegionalEmployee, pk=pk)
        regional_employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self,request,pk):
        if pk is not None:
            user = get_object_or_404(User, pk=pk)
            return Response(user.email, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# TouristAPIView

class TouristAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        if pk is not None:
            user = User.objects.filter(email=pk)
            id = user[0].id
            tourist = get_object_or_404(Tourist, pk=id)
            serializer = TouristSerializer(tourist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tourists = Tourist.objects.all()
        serializer = TouristSerializer(tourists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
            ],
        request_body=TouristSerializer)
    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TouristSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
            ],
        request_body=TouristSerializer)
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

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
    def delete(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        tourist = get_object_or_404(Tourist, pk=pk)
        tourist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# EventAPIView
class EventAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Event.objects.all()
        point_of_interest = self.request.query_params.get('point_of_interest')

        if point_of_interest:
            queryset = queryset.filter(point_of_interest=point_of_interest)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest', openapi.IN_QUERY, description='point_of_interest name', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self,request,pk):
        if pk is not None:
            event = get_object_or_404(Event, pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=EventSerializer)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            point_of_interest = serializer.validated_data.get('point_of_interest')
            if not (IsCentralEmployee().has_permission(request, self) or
                    IsRegionalEmployee().has_permission(request, self, city)):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=EventSerializer)
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

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
    def delete(self, request, pk):

        event = get_object_or_404(Event, pk=pk)
        city = event.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# TransportationAPIView

class TransportationAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
        if pk is not None:
            transportation = get_object_or_404(Transportation, pk=pk)
            serializer = TransportationSerializer(transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        transportations = Transportation.objects.all()
        serializer = TransportationSerializer(transportations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=TransportationSerializer)
    def post(self, request):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TransportationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=TransportationSerializer)
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


    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
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
        tourist = self.request.query_params.get('tourist')

        if tourist:
            queryset = queryset.filter(tourist=tourist)

        return queryset
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('tourist', openapi.IN_QUERY, description='tourist email', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self,request,pk):
        if pk is not None:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            if not IsTourist().has_permission(request, self):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=CommentSerializer)
    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            if not IsTourist().has_permission(request, self, comment):
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if not (IsCentralEmployee().has_permission(request, self) or 
                IsTourist().has_permission(request, self, comment)):
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
    def get(self,request,pk):
        if pk is not None:
            point_of_interest = get_object_or_404(PointOfInterest, pk=pk)
            serializer = PointOfInterestSerializer(point_of_interest)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = self.get_queryset()
        serializer = PointOfInterestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=PointOfInterestSerializer)
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

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=PointOfInterestSerializer)
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


    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
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
        point_of_interest = self.request.query_params.get('point_of_interest')

        if point_of_interest:
            queryset = queryset.filter(point_of_interest=point_of_interest)

        return queryset
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest', openapi.IN_QUERY, description='point_of_interest_name', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self,request,pk):
        if pk is not None:
            poi_transportation = get_object_or_404(PointOfInterest_Transportation, pk=pk)
            serializer = PointOfInterestTransportationSerializer(poi_transportation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        serializer = PointOfInterestTransportationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=PointOfInterestTransportationSerializer)
    def post(self, request):
        serializer = PointOfInterestTransportationSerializer(
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
    
    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
        request_body=PointOfInterestTransportationSerializer)
    def put(self, request, pk):
        if not IsCentralEmployee().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)

        poi_transportation = get_object_or_404(PointOfInterest_Transportation, pk=pk)
        serializer = PointOfInterestTransportationSerializer(
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


    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
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


# PhotoAPIView

class PhotoAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Photo.objects.all()
        point_of_interest = self.request.query_params.get('point_of_interest')

        if point_of_interest:
            queryset = queryset.filter(point_of_interest=point_of_interest)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest', openapi.IN_QUERY, description='point_of_interest_name', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self,request,pk):
        if pk is not None:
            photo = get_object_or_404(Photo, pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer Token',
                type=openapi.TYPE_STRING
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_of_interest': openapi.Schema(type=openapi.TYPE_INTEGER),
                'image': openapi.Schema(type=openapi.TYPE_FILE)
            },
            required=['point_of_interest', 'image']
        )
    )
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer Token',
                type=openapi.TYPE_STRING
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_of_interest': openapi.Schema(type=openapi.TYPE_INTEGER),
                'image': openapi.Schema(type=openapi.TYPE_FILE)
            },
            required=['point_of_interest', 'image']
        )
    )
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

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
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
        point_of_interest = self.request.query_params.get('point_of_interest')

        if point_of_interest:
            queryset = queryset.filter(point_of_interest=point_of_interest)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('point_of_interest', openapi.IN_QUERY, description='point_of_interest_name', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self,request,pk):
        if pk is not None:
            video = get_object_or_404(Video, pk=pk)
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer Token',
                type=openapi.TYPE_STRING
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_of_interest': openapi.Schema(type=openapi.TYPE_INTEGER),
                'video': openapi.Schema(type=openapi.TYPE_FILE)
            },
            required=['point_of_interest', 'video']
        )
    )
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description='Bearer Token',
                type=openapi.TYPE_STRING
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_of_interest': openapi.Schema(type=openapi.TYPE_INTEGER),
                'video': openapi.Schema(type=openapi.TYPE_FILE)
            },
            required=['point_of_interest', 'video']
        )
    )
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

    @swagger_auto_schema(
        manual_parameters=[
                openapi.Parameter(
                    'Authorization',
                    openapi.IN_HEADER,
                    description='Bearer Token',
                    type=openapi.TYPE_STRING
                )
        ],
    )
    def delete(self, request, pk):
        video = get_object_or_404(Video, pk=pk)
        point_of_interest = video.point_of_interest
        city = point_of_interest.city
        if not (IsCentralEmployee().has_permission(request, self) or
                IsRegionalEmployee().has_permission(request, self, city)):
            return Response(status=status.HTTP_403_FORBIDDEN)

        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)