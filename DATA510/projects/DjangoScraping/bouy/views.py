from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from lxml import html, etree
import urllib.request
import requests


@csrf_exempt
def index(request):

    if request.is_ajax():
        print('MADE IT HERE')

        url = 'https://www.ndbc.noaa.gov/station_page.php?station=41004'

        html = urllib.request.urlopen(url).read()
        # page = requests.get(url)
        # bouy_page = html.fromstring(page.text)


        table = etree.HTML(html).find("/table")
        rows = iter(table)
        headers = [col.text for col in next(rows)]
        for row in rows:
            values = [col.text for col in row]
            print(dict(zip(headers, values)))





        # soup = BeautifulSoup(html)
        # table = soup.find_all('table')
        # output_rows = []
        # for table_row in table[2].find_all('tr'):
        #     columns = table_row.find_all('td')
        #     output_row = []
        #     for column in columns:
        #         output_row.append(column.text)
        #     output_rows.append(output_row)
        # print('+++++++++++++++++++++++++++++++++++++++++++++')
        # for table_row in table[2].find_all('tr'):
        #     columns = table_row.findAll('td')
        #     output_row = []
        #     for column in columns:
        #         output_row.append(column.text)
        #     output_rows.append(output_row)
        # print('+++++++++++++++++++++++++++++++++++++++++++++')
        # for table_row in table[3].find_all('tr'):
        #     columns = table_row.findAll('td')
        #     output_row = []
        #     for column in columns:
        #         output_row.append(column.text)
        #     output_rows.append(output_row)
        # print('+++++++++++++++++++++++++++++++++++++++++++++')
        # for table_row in table[4].find_all('tr'):
        #     columns = table_row.findAll('td')
        #     output_row = []
        #     for column in columns:
        #         output_row.append(column.text)
        #     output_rows.append(output_row)
        # print('+++++++++++++++++++++++++++++++++++++++++++++')
        # for table_row in table[5].find_all('tr'):
        #     columns = table_row.findAll('td')
        #     output_row = []
        #     for column in columns:
        #         output_row.append(column.text)
        #     output_rows.append(output_row)




        # soup = BeautifulSoup(html,features="lxml")
        # tables = soup.find_all('table')
        # for table in tables:
        #     output_rows = []
        #     for table_row in table.findAll('tr'):
        #         columns = table_row.findAll('td')
        #         output_row = []
        #         for column in columns:
        #             output_row.append(column.text)
        #         output_rows.append(output_row)


        # tables = []
        # for table in bouy_page.xpath('//table'):
        #     # tables.append(table)
        #     print('+++++++++++++++++++++++++++++++++++++++++++++')
        #     print('+++++++++++++++++++++++++++++++++++++++++++++')
        #     print(table.text_content())
        #     print('+++++++++++++++++++++++++++++++++++++++++++++')
        #     print('+++++++++++++++++++++++++++++++++++++++++++++')
        #     print('+++++++++++++++++++++++++++++++++++++++++++++')

        # print(tables[0])

    template = loader.get_template('bouy/index.html')
    # return HttpResponse(template.render(myDictionary,request))
    return HttpResponse(template.render({}, request))