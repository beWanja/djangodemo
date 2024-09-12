# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import mydata


# Create your views here.

def myview(request):

    mynames = mydata.objects.all().values()    
    # to use the templates we create in the templates folder...
    template = loader.get_template('firstapp.html')
    context = {
        'mynames': mynames,
    }
    return HttpResponse(template.render(context, request))
    # below was the first little thingy i worked on
    # return HttpResponse("This is my first webpage! That should not have been this stressful tbh...")

# this view deals with incoming requests from the details url
def details(request, id):
    myname = mydata.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myname': myname,
    }

    return HttpResponse(template.render(context, request))