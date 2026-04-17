from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request))

def moviesingle(request):
    context = {}
    template = loader.get_template("moviesingle.html");
    return HttpResponse(template.render(context, request))

    