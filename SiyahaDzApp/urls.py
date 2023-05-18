from django.urls import path
from .views import *

urlpatterns = [
    path('regions/', regions, name='region-list'),
    path('regions/create/', RegionCreateAPIView.as_view(), name='region-create'),
    path('regions/<int:pk>/update/',
         RegionUpdateAPIView.as_view(), name='region-update'),
    path('regions/<int:pk>/delete/',
         RegionDeleteAPIView.as_view(), name='region-delete'),
]
