from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page2/$',views.page2, name='page2' ),
    url(r'^map/$',views.map, name='map' ),
    url(r'^login/$',views.login, name='login' ),
    url(r'^logincheck/$',views.loginCheck, name='loginCheck' ),
    url(r'^signup/$',views.signUp, name='signUp' ),
    url(r'^sign/$',views.sign, name='sign' ),
    url(r'^firstpage/$',views.firstPage, name='firstPage' ),
    url(r'^newtime/(?P<day>[1-7])/$',views.newTime, name='newTime' ),
    url(r'^getorder/$', views.getorder, name='getorder'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^sendmsg/$', views.sendmsg, name='sendmsg'),
    url(r'^checkmsg/$', views.checkmsg, name='checkmsg'),
    url(r'^order/$', views.order, name='order'),

]
