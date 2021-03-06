from django.contrib import admin
from .models import People,Place,Time

# Register your models here.

class TimeInLine(admin.TabularInline):
    model = Time
    extra = 0


class PeopleAdmin(admin.ModelAdmin):
    inlines = [TimeInLine]
    list_display = ('name','tel','place_name')
    list_filter = ['place__place_name']

    def place_name(self,obj):
        return obj.place.place_name




admin.site.register(Place)
admin.site.register(People,PeopleAdmin)
