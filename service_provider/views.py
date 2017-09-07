from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect

from service_provider.myFuncs.mapFunc import place_lonlat, place_time
from service_provider.myFuncs.order import getOrder
from service_provider.myFuncs.signupFunc import signUpCheck,signUpDb
from service_provider.myFuncs.index import welcomePage
from service_provider.myFuncs.login import loginCk,login1,loginSkip
from service_provider.myFuncs.time import getTime,setTime
from .models import Place
from service_provider.myFuncs.message import sendMsg,checkMsg



def map(request):
    places=Place.objects.values_list('place_name',flat=True)

    places_time_json=place_time(places)
    places_lonlat_json=place_lonlat(places)

    return render(request,'map.html',{'places_time_json':places_time_json,'places_lonlat_json':places_lonlat_json})

@csrf_protect
def login(request):
    if request.method=="POST":
        return login1(request)
    elif loginSkip(request):
        return HttpResponseRedirect('../firstpage')
    else:
        return render(request,'login.html')

@csrf_protect
def loginCheck(request):
    return loginCk(request)

@csrf_protect
def signUp(request):
    if request.method=="POST":
        return signUpCheck(request)
    else:
        return render(request,'signup.html')

@csrf_protect
def sign(request):
    if request.method=="POST":
        signUpDb(request)
        return HttpResponseRedirect('../firstpage')

def firstPage(request):
    return render(request,'index.html',welcomePage(request))

def newTime(request,day):
    if request.method=="GET":
        time, num = getTime(request, day)
        return render(request, 'service_time.html', {"time": time, "num": num, "day": day})
    else:
        setTime(request,day)
        return HttpResponseRedirect('../'+day)





def page2(request):
    return render(request,'page2.html')

def getorder(request):

    return render(request, 'getorder.html', getOrder(request))

def logout(request):
    del request.session["name"]
    del request.session["psd"]
    return HttpResponseRedirect('../login')


def sendmsg(request):
    phone = request.POST.get("tel", 0)
    sendMsg(phone)
    return HttpResponse(200)

def checkmsg(request):
    phone = request.POST.get("tel", 0)
    code = request.POST.get("code",0)
    if checkMsg(phone,code)!=200:
        return JsonResponse({"check_code": 0})
    else:
        return JsonResponse({"check_code": 1})

def order(request):
    return HttpResponse(200)

