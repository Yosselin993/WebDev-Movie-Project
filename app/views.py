from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    slObj = SocialLink.objects.all()
    sliderObj = Slider.objects.all()
    MTObj = MovieTheater.objects.all()
    adObj = Advertisement.objects.all()
    CelObj = Celebrity.objects.all()

    # adding the trailer(+ traileritem) and news(+ tweet) section 
    trailerObj = Trailer.objects.all()
    trailerItemObj = TrailerItem.objects.all()
    
    featuredNewsObj = News.objects.filter(section="featured") # splitting news to featured and more to match base
    moreNewsObj = News.objects.filter(section="more")


    tweetObj = Tweet.objects.all()

    #we need to put all the model refercences here like an array 
    context = {"SocialLink": slObj,
                "Slider": sliderObj,
                "MovieTheater": MTObj,
                "Advertisement": adObj,
                "Celebrity": CelObj, 
                "Trailer": trailerObj,
                "TrailerItem": trailerItemObj,
                "FeaturedNews": featuredNewsObj,
                "MoreNews": moreNewsObj, 
                "Tweet": tweetObj,
               
              }
    template = loader.get_template("base.html");
    return HttpResponse(template.render(context, request))

# def moviesingle(request):
#     context = {}
#     template = loader.get_template("moviesingle.html");
#     return HttpResponse(template.render(context, request))


#dont do this!(this was the incorrect way) we do not have to create a whole new enter point 
# def soicallink(request):
#     slObj = SocialLink.objects.all()
#     context= {"SocialLink": slObj}
#     template = loader.get_template("base.html")
#     return HttpResponse(template.render(context, request))

    