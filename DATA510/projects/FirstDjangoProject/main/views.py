from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from random import shuffle
from .models import *
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
import requests
import time
import json



def render_to_json_response(context, **response_kwargs):
   data = json.dumps(context)
   response_kwargs['content_type'] = 'application/json'
   return HttpResponse(data, **response_kwargs)


@csrf_exempt
def index(request):

    if request.is_ajax():

        browser = webdriver.Chrome("/home/thomas/git/datascience/MSDataSci/DATA510/projects/FirstDjangoProject/driver/chromedriver")

        browser.get('https://www.alltrails.com/us/south-carolina')
        for el in range(2):
            try:
                loadElement = browser.find_elements_by_xpath("//div[@class='feed-item load-more trail-load']")
                loadElement.click()
                time.sleep(4)
            except:
                break

        allTrails = browser.find_elements_by_xpath("//h3[@class='name xlate-none short']")

        a = open("a.csv", "w")

        for trail in allTrails:
            aElement = trail.find_element_by_tag_name('a')
            trailLink = aElement.get_attribute('href')

            browserPage = webdriver.Chrome("/home/thomas/git/datascience/MSDataSci/DATA510/projects/FirstDjangoProject/driver/chromedriver")
            browserPage.get(trailLink)
            rElements = browserPage.find_elements_by_xpath("//span[@class='detail-data xlate-none']")
            a.write(trail.text + ", " + trailLink + "\n")


            newTrail = Trail(trail_name=trail.text,
                                trail_length=float(rElements[0].text.split(' ')[0]),
                                trail_elevation=float(rElements[1].text.split(' ')[0].replace(',','')))
            newTrail.save()

            print(trail.text + ", " + rElements[0].text + ", " + rElements[1].text)
            

            time.sleep(4)
            browserPage.close()
        a.close()





    ##### ZIP CODE API

        # zipCode = request.POST.get('myVariableKey')
        # r = requests.get('http://api.zippopotam.us/us/' + zipCode)
        # print(str(r))
        # d = r.json()
        # print(d)
        # return render_to_json_response(d)




    ##### DJANGO ORM

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