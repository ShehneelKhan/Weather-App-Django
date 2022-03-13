from subprocess import list2cmdline
from django.shortcuts import render
from django.http import HttpResponse, request

import urllib
from urllib import request
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

       # source = urllib.request('api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city,"metric","b42bb8161af0ec32c58590d3773ed3f4")).read()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=b42bb8161af0ec32c58590d3773ed3f4').read()
        list_of_data = json.loads(source.decode('utf-8'))
        

        context = {
            'country' : str(list_of_data['sys']['country']),
            'temperature': str(list_of_data['main']['temp']),
            'feels_like': str(list_of_data['main']['feels_like']),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'wind_speed': str(list_of_data['wind']['speed']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }

       

    else:

        context = {}

    return render(request, "weather_app/index.html", context)
    

def about(request):
    return HttpResponse("Welcome to About Page!")


