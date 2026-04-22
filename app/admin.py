from django.contrib import admin
from .models import *

# Register your models here.

# 10 models to register on admin panel:

admin.site.register(SocialLink)
admin.site.register(Trailer)
admin.site.register(Slider)
admin.site.register(Advertisement)
admin.site.register(TrailerItem)
admin.site.register(Celebrity)
admin.site.register(News)
admin.site.register(Tweet)
admin.site.register(MovieTheater)
admin.site.register(MovieTV)