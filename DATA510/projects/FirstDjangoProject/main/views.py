from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from random import shuffle
from .models import *

def index(request):

    # allStudents = Student.objects.all()
    # allStudents = Student.objects.filter(student_age__gt=25).order_by('student_age')
    allStudents = Student.objects.all().order_by('student_age')
    # print(allStudents)

    myList = list(range(1,101))
    shuffle(myList)
    # print(myList)

    curRow = Student.objects.filter(first_name="Malcolm")[0]
    curRow.student_age = 56
    curRow.save()


    if len(Student.objects.filter(first_name="Michael")) == 0:
        newRow = Student(first_name="Michael",
                         last_name="L",
                         student_age=58)
        newRow.save()

    # myDictionary = {'myListKey':myList}
    myDictionary = {'myListKey': myList, 'allStudentsKey': allStudents}

    template = loader.get_template('main/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render(myDictionary, request))