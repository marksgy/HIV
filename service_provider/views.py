import datetime
from django.shortcuts import render
import json
from .models import People,Place,Time

# 将时间转换为json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def index(request):
    places=Place.objects.values_list('place_name',flat=True)

    names=locals()

    places_time=[]

    for place in places:
        names['%s_people' % place]=People.objects.filter(place__place_name=place)
        names['%s_time' % place]=Time.objects.filter(people__people_name=names['%s_people' % place][0].people_name).values_list('day_in_week','time_begin','time_end')
        for people in names['%s_people' % place]:
            a = Time.objects.filter(people__people_name=people.people_name).values_list('day_in_week','time_begin','time_end')
            names['%s_time' % place]=names['%s_time' % place]|a
        names['%s_time' % place]=names['%s_time' % place].distinct()
        places_time.append(list(names['%s_time' % place]))
# 地点-时间json
    places_time_json=json.dumps(places_time,cls=ComplexEncoder)







