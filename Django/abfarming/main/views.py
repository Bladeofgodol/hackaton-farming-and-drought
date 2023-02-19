from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import farmer
from .forms import Regform
import requests


def index(request):
    return render(request,'newhome.html')

def signin(request):
    return render(request,'newsignin.html')

def signup(request):
    context = {}
    if request.POST:
        form = Regform(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            user = form.save()
            login(request, user)

            return redirect('psignup')
        else:
            context['registration_form'] = form
    else:
        form = Regform()
        context['registration_form'] = form
    return render(request,'newsignup.html',context)

def signedindex(request):
    
    return render(request,'login_home.html')


def weather(request):
    #pull data from third party rest api
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=9.01&longitude=38.77&hourly=temperature_2m,apparent_temperature,precipitation,rain,showers,shortwave_radiation_instant,direct_radiation_instant,diffuse_radiation_instant,direct_normal_irradiance_instant,terrestrial_radiation_instant&daily=uv_index_max,uv_index_clear_sky_max,precipitation_sum,rain_sum,showers_sum&current_weather=true&timezone=auto')
    #convert reponse data into json
    users = response.json()
    print(users)
    return render(request,"login_home.html",{'datas': users})
    pass

def ct(request):
    return render(request,'crop_type.html')

def ctd (requst):
    return render(requst,'crop_detail.html')

def rlist(request):
    return render(request,'region_list.html')

def rdetail(request):
    return render(request,'region_detail.html')

def forum(request):
    return render(request,'newforum.html')

def contactus(request):
    return render(request,'newcontactus.html')


# Create your views here.
