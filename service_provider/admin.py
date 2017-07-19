from django.contrib import admin
from .models import People,Place,Time

# Register your models here.

class TimeInLine(admin.TabularInline):
    model = Time
    extra = 1

#
# class PeopleInLine(admin.TabularInline):
#     model = People
#     inlines =[TimeInLine]
#     extra = 3
#
# class PlacePeopleTimeInline(admin.TabularInline):
#     model = PlacePeopleTime
#
#
class PeopleAdmin(admin.ModelAdmin):
    inlines = [TimeInLine]
    list_display = ('people_name','tel_num','place_name')
    list_filter = ['place__place_name']

    def place_name(self,obj):
        return obj.place.place_name

# class PlaceAdmin(admin.ModelAdmin):
#     inlines = [PlacePeopleTimeInline]



admin.site.register(Place)
admin.site.register(People,PeopleAdmin)
