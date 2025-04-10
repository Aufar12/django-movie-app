from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    language = models.CharField(max_length=100)
    mpaa_type = models.CharField(max_length=10)
    mpaa_label = models.CharField(max_length=255)
    userRating = models.FloatField(
    validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.name

