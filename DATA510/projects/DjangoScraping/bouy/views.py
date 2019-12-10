from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from lxml import html, etree
from datetime import datetime
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


        numbers = re.compile('\d+(?:[\.\:]\d+(?:\s))?[ap]?m?')

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



        ############################################################
        # CurrentCondition
        ############################################################

        row_lim = 1
        col_lim = 1

        matrix = []
        row_count = 1
        for row in CurrentCondition_table.find_all('tr'):
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
                                cur_col.append(numbers.findall(str(column))[0])
                            else:
                                if column == '-':
                                    cur_col.append(None)    
                                else:
                                    cur_col.append(str(column).lstrip().rstrip())
                    col_count+=1
            if len(cur_col) > 0:
                matrix.append(cur_col)
            row_count+=1

        print('\n\nCurrentCondition data:\n' + str(matrix))

        from bouy.models import CurrentCondition
        CurrentCondition.objects.all().delete()
        for row in matrix:
            data_datetime = '2019-'+str(row[0])+'-'+str(row[1])+'T'+str(row[2]).replace(u'\xa0', u'')
            new_row = CurrentCondition(
                Location=location,
                DateTime=datetime.strptime(data_datetime, '%Y-%m-%dT%H:%M%p'),
                WDIR=row[3],
                WSPD=row[4],
                GST=row[5],
                WVHT=row[6],
                DPD=row[7],
                APD=row[8],
                MWD=row[9],
                PRES=row[10],
                PTDY=row[11],
                ATMP=row[12],
                WTMP=row[13],
                DEWP=row[14],
                SAL=row[15],
                VIS=row[16],
                TIDE=row[17]
                )
            new_row.save()



        ############################################################
        # DetailWave
        ############################################################

        row_lim = 1
        col_lim = 1

        matrix = []
        row_count = 1
        for row in DetailWave_table.find_all('tr'):
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
                                cur_col.append(numbers.findall(str(column))[0])
                            else:
                                if column == '-':
                                    cur_col.append(None)    
                                else:
                                    cur_col.append(str(column).lstrip().rstrip())
                    col_count+=1
            if len(cur_col) > 0:
                matrix.append(cur_col)
            row_count+=1

        print('\n\nDetailWave data:\n' + str(matrix))

        from bouy.models import DetailWave
        DetailWave.objects.all().delete()
        for row in matrix:
            data_datetime = '2019-'+str(row[0])+'-'+str(row[1])+'T'+str(row[2]).replace(u'\xa0', u'')
            new_row = DetailWave(
                Location=location,
                DateTime=datetime.strptime(data_datetime, '%Y-%m-%dT%H:%M%p'),
                WVHT=row[3],
                SwH=row[4],
                SwP=row[5],
                SwD=row[6],
                WWH=row[7],
                WWP=row[8],
                WWD=row[9],
                STEEPNESS=row[10]
                )
            new_row.save()


    template = loader.get_template('bouy/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render({}, request))