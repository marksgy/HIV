from django.shortcuts import render_to_response
import json
import weixin.models
from .models import UserInfo,OrderInfo

# Create your views here.

def index(request):
    if request.method =="POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        qq = request.POST.get("qq", None)
        email = request.POST.get("email", None)
        #print(username,password)

    return render_to_response(request,'index.html')

