from django.contrib import admin

# Register your models here.

from .models import OrderInfo, UserInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','email', 'qq')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','phone','methods','place','name1','tel','time')

    def name(self,obj):
        return obj.user.name

    def phone(self,obj):
        return obj.user.phone

    def place(self,obj):
        return obj.service.place.place_name

    def name1(self,obj):
        return obj.service.name

    def tel(self,obj):
        return obj.service.tel







admin.site.register(OrderInfo, OrderAdmin)
admin.site.register(UserInfo, UserAdmin)