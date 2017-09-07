from django.http import JsonResponse

from ..models import People




def signUpCheck(request):
    phone = request.POST.get("tel", 0)
    es = People.objects.filter(tel=phone).exists()
    if not es:
        return JsonResponse({"check_code": 0})
    else:
        people = People.objects.get(tel=phone)
        psd=people.psd
        if psd=='':
            return JsonResponse({"check_code": 1})
        else:
            return JsonResponse({"check_code": 2})


def signUpDb(request):
    phone = request.POST.get("userName", 0)
    psd=request.POST.get('psdEncode',0)
    people=People.objects.get(tel=phone)
    people.psd=psd
    name=people.name
    people.save()
    request.session['name']=name
    request.session['psd']=psd


