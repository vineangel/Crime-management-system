"""projectcrime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  
from.import views

urlpatterns = [
    path('signup.html',views.signup,name='signup'),
    path('login', views.login, name='login'),
    path('test.html', views.test, name='test'),
    path('test.py', views.testpy, name='testpy'),
    path('test1.html', views.save_image, name='save_image'),
    path('test3.html', views.test3, name='test3'),
    path('test4.html', views.test4, name='test4'),
    path('savepicture.py', views.savepicture, name='savepicture'),
    path('', views.login, name='login'),
    path('policeindex.html',views.policeindex,name='policeindex'),
    path('userindex.html',views.userindex,name='userindex'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('filecomplaint.html',views.filecomplaint,name='filecomplaint'),
    path('policeviewcomplaints.html',views.policeviewcomplaints,name='policeviewcomplaints'),
    path('policeupdatecomplaintstatus.html',views.policeupdatecomplaintstatus,name='policeupdatecomplaintstatus'),
    path('police_view_criminals.html',views.police_view_criminals,name='police_view_criminals'),
    path('profile.html', views.profile, name='profile'),
    path('policeprofile.html', views.policeprofile, name='policeprofile'),
    path('updateprofile.html', views.updateprofile, name='updateprofile'),
    path('policeupdateprofile.html', views.policeupdateprofile, name='policeupdateprofile'),
    path('addcriminaldetails.html', views.addcriminaldetails, name='addcriminaldetails'),
    path('updatecriminalstatus.html', views.updatecriminalstatus, name='updatecriminalstatus'),
    path('user_view_complaint.html', views.user_view_complaint, name='user_view_complaint'),
    path('policeaddnews.html', views.policeaddnews, name='policeaddnews'),
    path('policeaddnews.html', views.countdbobject, name='countdbobject'),
    path('contact', views.contactview, name='contactview'),
    path('delete', views.delete),
    path('logout', views.logout, name='logout'),
    path('some.html', views.usersave, name='usersave'),
    path('usersave', views.usersave, name='usersave'),
    path('save_image.html', views.save_image, name='save_image'),
    path('policeviewrelatedcrimes.html/<str:suspect>/', views.policeviewrelatedcrimes, name='policeviewrelatedcrimes'),
    # path('policeviewrelatedcrimes.html', views.policeviewrelatedcrimes, name='policeviewrelatedcrimes'),

]