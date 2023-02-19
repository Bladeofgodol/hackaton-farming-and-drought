from django.shortcuts import render


def index(request):
    return render(request,'newhome.html')

def signin(request):
    return render(request,'newsignin.html')

def signup(request):
    return render(request,'newsignup.html')

def signedindex(request):
    return render(request,'login_home.html')

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
