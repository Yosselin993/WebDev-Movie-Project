from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    context = {}
    template = loader.get_template("base.html");
    return HttpResponse(template.render(context, request))

def moviesingle(request):
    context = {}
    template = loader.get_template("moviesingle.html");
    return HttpResponse(template.render(context, request))

def soicallink(request):
    slObj = SocialLink.objects.all()
    context= {"SocialLink": slObj}
    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))

    