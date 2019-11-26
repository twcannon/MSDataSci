from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from lxml import html, etree
import urllib.request
import requests
import re


@csrf_exempt
def index(request):

    if request.is_ajax():
        location = '41004'

        print('Scraping Data for Bouy ID: '+str(location))

        url = 'https://www.ndbc.noaa.gov/station_page.php?station='+location

        html = urllib.request.urlopen(url).read()
        # page = requests.get(url)
        # bouy_page = html.fromstring(page.text)


        soup = BeautifulSoup(html, 'lxml') # Parse the HTML as a string
        contenttable = soup.find('table', id='contenttable').find('td', id='contentarea') # Grab the first table
        tables = contenttable.find_all('table') # Grab the first table
        
        CurrentWind_table = tables[1] # skip first tr
        HighestOneMinWind_table = tables[2].find('table')
        CurrentCondition_table = tables[4] # skip first two tr
        CurrentWave_table = tables[5] # skip first tr
        DetailWave_table = tables[6] # skip first two tr


        numbers = re.compile('\d+(?:\.\d+)?')

        ############################################################
        # CurrentWind
        ############################################################

        row_lim = 2
        col_lim = 3

        matrix = []
        row_count = 1
        for row in CurrentWind_table.find_all('tr'):
            # print('row_count: '+str(row_count))
            if row_count >= row_lim:
                # print(row)
                columns = row.find_all('td')
                cur_col = []
                col_count = 1
                for column in columns:
                    # print('col_count: '+str(col_count) + 'column: '+str(column))
                    if col_count >= col_lim and column is not None:
                        td = BeautifulSoup(str(column), 'lxml')
                        column = td.find('td').getText()
                        if column != '':
                            if len(numbers.findall(str(column))) > 0:
                                matrix.append(numbers.findall(str(column))[0])
                            else:
                                matrix.append(str(column).lstrip())
                    col_count+=1
            row_count+=1

        print('\n\nCurrentWind data:\n' + str(matrix))

        from bouy.models import CurrentWind
        CurrentWind.objects.all().delete()
        new_row = CurrentWind(
            Location=location,
            WDIR=matrix[0],
            WSPD=matrix[1],
            GST=matrix[2],
            PRES=matrix[3],
            WTMP=matrix[4],
            WSPD10M=matrix[5],
            WSPD20M=matrix[6]
            )
        new_row.save()






        ############################################################
        # CurrentWave
        ############################################################


        row_lim = 2
        col_lim = 3

        matrix = []
        row_count = 1
        for row in CurrentWave_table.find_all('tr'):
            # print('row_count: '+str(row_count))
            if row_count >= row_lim:
                # print(row)
                columns = row.find_all('td')
                cur_col = []
                col_count = 1
                for column in columns:
                    # print('col_count: '+str(col_count) + 'column: '+str(column))
                    if col_count >= col_lim and column is not None:
                        td = BeautifulSoup(str(column), 'lxml')
                        column = td.find('td').getText()
                        if column != '':
                            if len(numbers.findall(str(column))) > 0:
                                matrix.append(numbers.findall(str(column))[0])
                            else:
                                matrix.append(str(column).lstrip())
                    col_count+=1
            row_count+=1

        print('\n\nCurrentWave data:\n' + str(matrix))

        from bouy.models import CurrentWave
        CurrentWave.objects.all().delete()
        new_row = CurrentWave(
            Location=location,
            WVHT=matrix[0],
            SwH=matrix[1],
            SwP=matrix[2],
            SwD=matrix[3],
            WWH=matrix[4],
            WWP=matrix[5],
            WWD=matrix[6],
            APD=matrix[7]
            )
        new_row.save()




        ############################################################
        # HighestOneMinWind
        ############################################################


        print(HighestOneMinWind_table)

        row_lim = 3
        col_lim = 1

        matrix = []
        row_count = 1
        for row in HighestOneMinWind_table.find_all('tr'):
            # print('row_count: '+str(row_count))
            if row_count >= row_lim:
                # print(row)
                columns = row.find_all('td')
                cur_col = []
                col_count = 1
                for column in columns:
                    # print('col_count: '+str(col_count) + 'column: '+str(column))
                    if col_count >= col_lim and column is not None:
                        td = BeautifulSoup(str(column), 'lxml')
                        column = td.find('td').getText()
                        if column != '':
                            if len(numbers.findall(str(column))) > 0:
                                matrix.append(numbers.findall(str(column))[0])
                            else:
                                matrix.append(str(column).lstrip())
                    col_count+=1
            row_count+=1

        print('\n\nHighestOneMinWind data:\n' + str(matrix))

        from bouy.models import HighestOneMinWind
        HighestOneMinWind.objects.all().delete()
        new_row = HighestOneMinWind(
            Location=location,
            TIME=matrix[0],
            WSPD=matrix[1],
            WDIR=matrix[2],
            )
        new_row.save()





    template = loader.get_template('bouy/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render({}, request))