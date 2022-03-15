from subprocess import list2cmdline
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import urllib
from urllib import request
import json

# Create your views here.
  

@login_required
def home(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city,"metric","b42bb8161af0ec32c58590d3773ed3f4")).read()
      
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

    return render(request, "weather_app/home.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Hi {}, your account was created successfully".format(username))
            return redirect('login')
    else:     
        form = UserRegistrationForm()


    context = {"form": form}
    return render(request, 'weather_app/register.html',context)



#THIS IS DONE AUTOMATICALLY BY AUTH_VIEW(see urls.py)
# def login(request):
#     return render(request, 'weather_app/login.html')


#THIS IS DONE AUTOMATICALLY BY AUTH_VIEW(see urls.py)
# def logout(request):
#     return render(request, 'weather_app/logout.html')


@login_required()
def profile(request):
    return render(request, "weather_app/profile.html")