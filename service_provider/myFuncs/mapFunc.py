import datetime
import json,decimal
from service_provider.models import People,Place,Time

names=locals()
# 将时间转换为json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)

# 获取地点-时间json
def place_time(place_names):
    places_time = {}
    for place in place_names:
        names['%s_people' % place] = People.objects.filter(place__place_name=place)
        names['%s_time' % place] = Time.objects.filter(
            people__name=names['%s_people' % place][0].name).values_list('day_in_week', 'time_begin',
                                                                                       'time_end')
        for people in names['%s_people' % place]:
            a = Time.objects.filter(people__name=people.name).values_list('day_in_week', 'time_begin',
                                                                                        'time_end')
            names['%s_time' % place] = names['%s_time' % place] | a
        names['%s_time' % place] = names['%s_time' % place].distinct()
        places_time[place] = list(names['%s_time' % place])
    places_time_json = json.dumps(places_time, cls=ComplexEncoder)
    return places_time_json

# 获取地点-坐标
def place_lonlat(place_names):
    places_lonlat = {}
    for place in place_names:
        names['%s_lonlat' % place] = Place.objects.filter(place_name=place).values_list('longtitude','latitude')

        places_lonlat[place] = list(names['%s_lonlat' % place])
        # 地点-时间json
    places_lonlat_json = json.dumps(places_lonlat,cls=DecimalJSONEncoder)
    return places_lonlat_json