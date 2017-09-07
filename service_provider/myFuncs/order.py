from service_provider.models import People
from weixin.models import OrderInfo


def getOrder(request):
    name = request.session.get('name', 'anybody')
    psd = request.session.get('psd', 'pad')
    people = People.objects.filter(name=name).filter(psd=psd)[0:1].get()
    orderinfo=OrderInfo.objects.filter(service=people).order_by("-time")
    if orderinfo.exists():
        order = orderinfo[0:1].get()

    method=order.get_methods_display()
    day_in_week=order.get_day_in_week_display()
    meettime=order.meettime
    username=order.user.name
    userphone=order.user.phone

    data={"method":method,"day_in_week":day_in_week,"meettime":meettime,"username":username,"userphone":userphone}

    return data


