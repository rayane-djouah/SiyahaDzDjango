from django.contrib import admin
from .models import *

# Register your models here.

class RegionalEmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'region')
    list_filter = ('region',)
    search_fields = ('user__username', 'region__name')

class CentralEmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

class TouristAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'point_of_interest', 'opendate', 'closedate']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['tourist', 'point_of_interest', 'comment']


class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'theme', 'city', 'latitude', 'longitude']


class TransportationAdmin(admin.ModelAdmin):
    list_display = ['name']

class PointOfInterest_TransportationAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'transportation']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'image']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'video']

admin.site.register(RegionalEmployee, RegionalEmployeeAdmin)
admin.site.register(CentralEmployee, CentralEmployeeAdmin)
admin.site.register(Tourist, TouristAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(PointOfInterest_Transportation, PointOfInterest_TransportationAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)