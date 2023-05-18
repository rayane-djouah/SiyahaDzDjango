from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Region views

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
      
class RegionCreateAPIView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    #permission_classes = [permissions.IsAuthenticated, IsCentralEmployee]

class RegionUpdateAPIView(generics.UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    #permission_classes = [permissions.IsAuthenticated, IsCentralEmployee]

class RegionDeleteAPIView(generics.DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    #permission_classes = [permissions.IsAuthenticated, IsCentralEmployee]
    
    
# City views 
    
class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return City.objects.filter(region_id=region_id)