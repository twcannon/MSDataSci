from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse

def index(request):


    template = loader.get_template('bouy/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render({}, request))