import json

import datetime

from ..models import Time,People

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def getTime(request,day):
    name = request.session.get('name', 'anybody')
    psd = request.session.get('psd', 'pad')
    people=People.objects.filter(name=name).filter(psd=psd)[0:1].get()
    time=Time.objects.filter(people=people).filter(day_in_week=day).distinct().values_list('time_begin', 'time_end')
    times= list(time)
    num=[]
    i=0
    while i < time.count():
        num.append(i)
        i=i+1

    timejson= json.dumps(times, cls=ComplexEncoder)
    return timejson,num

def setTime(request,day):
    name = request.session.get('name', 'anybody')
    psd = request.session.get('psd', 'pad')
    people = People.objects.filter(name=name).filter(psd=psd)[0:1].get()
    Time.objects.filter(people=people).filter(day_in_week=day).delete()
    for i in range(1,100):
        beginH="beginH"+str(i)
        beginM="beginM"+str(i)
        endH="endH"+str(i)
        endM="endM"+str(i)

        bH0 = request.POST.get(beginH, "0")
        bM0 = request.POST.get(beginM, "0")
        eH0 = request.POST.get(endH, "0")
        eM0 = request.POST.get(endM, "0")



        bH=int(bH0)


        bM=int(bM0)


        eH=int(eH0)


        eM=int(eM0)

        if bH<0 or bH>=24 or bM<0 or bM>=60 or eH<0 or eH>=24 or eM<0 or eM>=60:
            break
        begin=datetime.datetime(2017, 1, 1, bH, bM, 0)
        end =datetime.datetime(2017, 1, 1,eH,eM,0)

        settime=Time()
        settime.day_in_week=day
        settime.time_begin=begin
        settime.time_end=end
        settime.people=people
        settime.save()





