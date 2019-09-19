from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from random import shuffle
from .models import *

def index(request):

    allStudents = Student.objects.all()

    myList = list(range(1,101))
    shuffle(myList)
    print(myList)

    # myDictionary = {'myListKey':myList}
    myDictionary = {'myListKey':myList,
                    'allStudentsKey': allStudents}

    template = loader.get_template('main/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render(myDictionary, request))