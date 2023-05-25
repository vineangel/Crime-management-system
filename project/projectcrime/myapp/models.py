from django.db import models
import itertools

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

class user_details(models.Model):
    user_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=200)
    gender = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    phone = models.IntegerField()
    userphoto = models.ImageField(null=True)

    def __str__(self):
        return self.name

class station(models.Model):
    station_name =models.CharField(max_length=100)

    def __str__(self):
        return self.station_name

class police_details(models.Model):
    police_name = models.CharField(max_length=100,null=True)
    police_birthday = models.CharField(max_length=200,null=True)
    police_gender = models.CharField(max_length=500,null=True)
    police_email = models.CharField(max_length=500,null=True)
    police_password = models.CharField(max_length=500,null=True)
    police_phone = models.IntegerField()
    police_department = models.CharField(max_length=100,null=True)
    rank = models.CharField(max_length=100,null=True)
    Badge_number = models.IntegerField()
    Batch = models.IntegerField()
    police_photo = models.ImageField(null=True)
    stationn = models.ForeignKey(station,on_delete=models.CASCADE,null=True)

class complaint(models.Model):
    complaint_title = models.CharField(max_length=100)
    complaint_details = models.CharField(max_length=100)
    suspect = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)
    phone = models.IntegerField( null=True)
    supporting_doc = models.FileField(upload_to ='uploads/')
    address = models.CharField(max_length=100)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    station = models.ForeignKey(station, on_delete=models.CASCADE)

class contact(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(user_details, on_delete=models.CASCADE)


class news(models.Model):
    newstitle = models.CharField(max_length=100)
    newscontent = models.CharField(max_length=200)
    newsimg = models.ImageField()

class criminaldetails(models.Model):
    criminalname = models.CharField(max_length=100)
    photo =models.ImageField(null=True)
    criminal_date_of_birth = models.DateField()
    criminal_gender = models.CharField(max_length=500)
    criminal_email = models.CharField(max_length=500)
    criminal_phone = models.IntegerField()
    crime = models.CharField(max_length=200)
    criminal_address = models.CharField(max_length=200)
    case_status = models.CharField(max_length=200)
    registered_station = models.CharField(max_length=100)
    identity = models.ImageField(null=True)
    evidence = models.ImageField(null=True)

class cimg(models.Model):
    cimage =models.ImageField(null=True)



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

from django.db import models

class WebcamImage(models.Model):
    image = models.ImageField(upload_to='webcam_images/')
    created_at = models.DateTimeField(auto_now_add=True)

class CDetails(models.Model):
    User_name = models.CharField(max_length= 300)
    User_phone = models.BigIntegerField()
    User_address = models.TextField()
    User_pic = models.FileField(upload_to='documents/%Y/%m/%d')

class xx(models.Model):

    User_pic = models.FileField(upload_to='documents/%Y/%m/%d')

class MyModel(models.Model):
    image = models.TextField()

    def __str__(self):
        return f"WebcamImage {self.pk}"
