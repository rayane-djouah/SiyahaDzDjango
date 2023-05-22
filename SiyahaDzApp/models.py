from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name
        
class RegionalEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='regionalemployee', primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CentralEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='centralemployee', primary_key=True)
    
    def __str__(self):
        return self.user.username

class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tourist', primary_key=True)
    
    def __str__(self):
        return self.user.username

class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name
    
class Transportation(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.tourist.username} - {self.point_of_interest.name}"

    def save(self, *args, **kwargs):
        self.id = f"{self.tourist.username}-{self.point_of_interest.name}"
        super().save(*args, **kwargs)

class OpeningHours(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.point_of_interest.name} - {self.day_of_week}"

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.day_of_week}"
        super().save(*args, **kwargs)

class PointOfInterest_Transportation(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.point_of_interest.name} - {self.transportation.name}"

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.transportation.name}"
        super().save(*args, **kwargs)
    
class Photo(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='storage/photos/')

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.image.name}"
        super().save(*args, **kwargs)


class Video(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    video = models.FileField(upload_to='storage/videos/')

    def __str__(self):
        return self.video.name

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.video.name}"
        super().save(*args, **kwargs)
