from django.db import models

# Create your models here.
from django.utils import timezone



class Place(models.Model):
    place_name=models.CharField(max_length=200)
    longtitude=models.DecimalField(default=0,max_digits=10,decimal_places=6)
    latitude = models.DecimalField(default=0,max_digits=10,decimal_places=6)



    def __str__(self):
        return self.place_name

class People(models.Model):
    place = models.ForeignKey(Place)
    people_name=models.CharField(max_length=200,primary_key=True)
    tel_num=models.CharField(max_length=11)


    def __str__(self):
        return self.people_name



class Time(models.Model):
    DAY_IN_WEEK=(
        ("1", "星期一"),
        ("2", "星期二"),
        ("3", "星期三"),
        ("4", "星期四"),
        ("5", "星期五"),
        ("6", "星期六"),
        ("7", "星期天"),
    )
    day_in_week=models.CharField(max_length=2,choices=DAY_IN_WEEK)
    time_begin=models.TimeField(default=timezone.now)
    time_end=models.TimeField(default=timezone.now)
    people=models.ForeignKey(People)


