from django.db import models
from django.contrib.auth.models import User

        
class RegionalEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='regionalemployee', primary_key=True)
    region = models.CharField(max_length=100)

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
    
    
class Transportation(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    category = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    views_count = models.IntegerField(default=0)
    openhour = models.TimeField
    closehour = models.TimeField
    
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    description = models.TextField()
    opendate = models.DateField()
    closedate = models.DateField()
    image = models.ImageField(upload_to="storage/photoevent/")
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    id = models.CharField(max_length=255, primary_key=True)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"{self.tourist.user.email} - {self.point_of_interest.name}"

    def save(self, *args, **kwargs):
        self.id = f"{self.tourist.user.email}-{self.point_of_interest.name}"
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
    image = models.ImageField(upload_to='storage/point_of_interest/photos')

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.image.name}"
        super().save(*args, **kwargs)


class Video(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    video = models.FileField(upload_to='storage/point_of_interest/videos')

    def __str__(self):
        return self.video.name

    def save(self, *args, **kwargs):
        self.id = f"{self.point_of_interest.name}-{self.video.name}"
        super().save(*args, **kwargs)
