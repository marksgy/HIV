from django.db import models

# Create your models here.
from django.utils import timezone



class Place(models.Model):
    place_name=models.CharField(max_length=50,primary_key=True)
    longtitude=models.DecimalField(default=0,max_digits=10,decimal_places=6)
    latitude = models.DecimalField(default=0,max_digits=10,decimal_places=6)



    def __str__(self):
        return self.place_name

class People(models.Model):
    place = models.ForeignKey(Place)
    name=models.CharField(max_length=50,primary_key=True)
    tel=models.CharField(max_length=11)
    psd=models.CharField(max_length=32,blank=True)



    def __str__(self):
        return self.name





class Time(models.Model):
    DAY_IN_WEEK=(
        (1, "星期一"),
        (2, "星期二"),
        (3, "星期三"),
        (4, "星期四"),
        (5, "星期五"),
        (6, "星期六"),
        (7, "星期天"),
    )
    day_in_week=models.IntegerField(choices=DAY_IN_WEEK)
    time=models.IntegerField()
    people=models.ForeignKey(People)





