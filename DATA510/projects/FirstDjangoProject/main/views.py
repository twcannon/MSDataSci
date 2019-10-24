from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from random import shuffle
from .models import *

from django.views.decorators.csrf import csrf_exempt

import requests

import json

def render_to_json_response(context, **response_kwargs):
   data = json.dumps(context)
   response_kwargs['content_type'] = 'application/json'
   return HttpResponse(data, **response_kwargs)


@csrf_exempt
def index(request):

    if request.is_ajax():
        # otherFunction()
        zipCode = request.POST.get('myVariableKey')
        r = requests.get('http://api.zippopotam.us/us/' + zipCode)
        print(str(r))
        d = r.json()
        print(d)
        return render_to_json_response(d)

    # # allStudents = Student.objects.all()
    # # allStudents = Student.objects.filter(student_age__gt=25).order_by('student_age')
    # allStudents = Student.objects.all().order_by('student_age')
    # # print(allStudents)

    # myList = list(range(1,101))
    # shuffle(myList)
    # # print(myList)

    # curRow = Student.objects.filter(first_name="Malcolm")[0]
    # curRow.student_age = 56
    # curRow.save()


    # if len(Student.objects.filter(first_name="Michael")) == 0:
    #     newRow = Student(first_name="Michael",
    #                      last_name="L",
    #                      student_age=58)
    #     newRow.save()

    # # myDictionary = {'myListKey':myList}
    # myDictionary = {'myListKey': myList, 'allStudentsKey': allStudents}

    template = loader.get_template('main/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render({}, request))