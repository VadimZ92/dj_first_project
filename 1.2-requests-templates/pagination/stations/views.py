from django.shortcuts import render, redirect
from django.urls import reverse
import csv, os
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    # return redirect(reverse('bus_stations'))
    return render(request, 'index.html')

bus_stations_list = []
with open('C:\\Users\\hemul\\Desktop\\Нетология\\projects\\django\\first_project\\dj-homeworks\\1.2-requests-templates\\pagination\\data-398-2018-08-30.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bus_stations_list.append(row)

def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        # 'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
