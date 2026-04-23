from django.db import models

# Create your models here.

# 10 total models from ER-Diagram: 

# id PK int from ER diagram is already being created by django

class SocialLink(models.Model):
    #idk about the ID field
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=50) #changed to 50 
    icon_class = models.CharField(max_length=30)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name;

class Trailer(models.Model):
    #idk about the ID field
    trailer_URL = models.CharField(max_length=200)

    def __str__(self):
        return self.trailer_URL;

# slider table with image info, anchor URL, movie info and rating range
class Slider(models.Model):
    image_src = models.CharField(max_length=200) # file path to slides's img
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    anchor_url = models.URLField(max_length=200) # url the slide links to when clicked
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5) # ex) lower = "8.5"
    upper_rating = models.CharField(max_length=5) # ex) upper = "9.0"


    def __str__(self):
        return self.movie_title

# advertisement table with a 'section' field to know where the display each add
class Advertisement(models.Model):
    section = models.CharField
    img_src = models.CharField(max_length=20)
    img_width = models.IntegerField()
    img_height = models.IntegerField()

    def __str__(self):
        return self.section
    
# trailerItem with image info, description, and duration
class TrailerItem(models.Model):
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField()
    img_height = models.IntegerField()   
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.description

# celebrity class with image, name, type, and link URLss
class Celebrity(models.Model):
    anchor_url = models.CharField(max_length=200)
    img_width = models.IntegerField()   
    img_height = models.IntegerField()   
    celebrity_url = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_type = models.CharField(max_length=20)

    def __str__(self):
        return self.celebrity_name

# class news with section, image, title. content, and time
class News(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField()  
    img_height = models.IntegerField()  
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# class tweet with just content (string/textfield)
class Tweet(models.Model):
    content = models.TextField() # is this the string?

    def __str__(self):
        return self.content[:50] # ':50' shows the first 50 characters in the admin panel as a preview

# class movietheater: stores movies shown in the 'in theaters' tab
class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

# class movietv: stores movies shown in the 'on tv' tab
class MovieTV(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title

