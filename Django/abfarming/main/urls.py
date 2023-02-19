from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('index/',views.signedindex,name='signedindex'),
    path('croptype/',views.ct,name='croptype'),
    path('cropdetail/',views.ctd,name='cropdetail'),
    path('regionlist/',views.rlist,name='regionlist'),
    path('regiondetail/',views.rdetail,name='regiondetail'),
    path('forum/',views.forum,name='forum'),
    path('contactus/',views.contactus,name='contactus'),
    
]
