from django.db import models
from django.utils import timezone

from service_provider import models as mymodels

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class OrderInfo(models.Model):
    CHECK_CHOICES = (
        ('B', '血检'),
        ('S', '唾检'),
    )
    methods = models.CharField(max_length=1, choices=CHECK_CHOICES)
    time = models.TimeField(default=timezone.now)
    DAY_IN_WEEK = (
        ("1", "星期一"),
        ("2", "星期二"),
        ("3", "星期三"),
        ("4", "星期四"),
        ("5", "星期五"),
        ("6", "星期六"),
        ("7", "星期天"),
    )
    day_in_week = models.CharField(max_length=1, choices=DAY_IN_WEEK)
    meettime=models.TimeField(default=timezone.now)
    user=models.ForeignKey(UserInfo)
    service=models.ForeignKey(mymodels.People)


    def __str__(self):
        return self.user.name+self.service.place.place_name+self.service.name


