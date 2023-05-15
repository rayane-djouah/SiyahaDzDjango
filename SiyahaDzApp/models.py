from django.contrib.auth.models import User
from django.db import models

class RegionalEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CentralEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.point_of_interest.name}"


class PointOfInterest(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class OpeningHours(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.point_of_interest.name} - {self.day_of_week}"

class Transportation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PointOfInterest_Transportation(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.point_of_interest.name} - {transportation.name}"   

class Photo(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='storage/photos/')

    def __str__(self):
        return self.image.name


class Video(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    video = models.FileField(upload_to='storage/videos/')

    def __str__(self):
        return self.video.name