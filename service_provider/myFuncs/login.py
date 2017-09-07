from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from ..models import People
def loginCk(request):
    phone = request.POST.get("tel", 0)
    psdEncode = request.POST.get('psdEncode',0)
    es = People.objects.filter(tel=phone).exists()
    if not es:
        return JsonResponse({"check_code": 0})
    else:
        people = People.objects.get(tel=phone)
        psd = people.psd
        if psd == psdEncode:
            return JsonResponse({"check_code": 1})
        else:
            return JsonResponse({"check_code": 2})

def login1(request):
    phone = request.POST.get("tel", 0)
    people = People.objects.get(tel=phone)
    psd = people.psd
    name = people.name
    request.session["name"]=name
    request.session["psd"] = psd
    return HttpResponseRedirect('../firstpage')

def loginSkip(request):
    if "name" in request.session:
        return True
    else:
        return False

