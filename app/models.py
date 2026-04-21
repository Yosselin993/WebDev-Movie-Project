from django.db import models

# Create your models here.

class SocialLink(models.Model):
    #idk about the ID field
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=2)
    icon_class = models.CharField(max_length=30)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name;

class Trailer(models.Model):
    #idk about the ID field
    trailer_URL = models.URLField(max_length=200)

    def __str__(self):
        return self.trailer_URL;