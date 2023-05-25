from django.contrib import admin

from django.contrib import admin
from .models import *

class user_detailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday','gender', 'phone', 'email')
class user_loginAdmin(admin.ModelAdmin):
    list_display = ('uname', 'password','u_type')
class complaintAdmin(admin.ModelAdmin):
    list_display = ('complaint_title', 'suspect','user')

# Register your models here.
admin.site.register(user_login,user_loginAdmin)
admin.site.register(user_details, user_detailsAdmin)
admin.site.register(police_details)
admin.site.register(station)
admin.site.register(complaint,complaintAdmin)
admin.site.register(news)
admin.site.register(criminaldetails)
admin.site.register(cimg)
admin.site.register(ImageModel)
admin.site.register(WebcamImage)
admin.site.register(xx)
admin.site.register(MyModel)
admin.site.register(contact)