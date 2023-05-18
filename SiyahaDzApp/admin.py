from django.contrib import admin
from .models import *

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['tourist', 'point_of_interest', 'comment']

class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'theme', 'city', 'latitude', 'longitude']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']

class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'day_of_week', 'opening_time', 'closing_time']

class TransportationAdmin(admin.ModelAdmin):
    list_display = ['name']

class PointOfInterest_TransportationAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'transportation']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'image']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['point_of_interest', 'video']

# Register your models with the customized ModelAdmin classes
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(PointOfInterest_Transportation, PointOfInterest_TransportationAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)