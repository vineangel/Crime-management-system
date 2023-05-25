import base64
import uuid

from django.shortcuts import render, redirect


from .models import *
from django.db.models import Max, Min
from django.core.files.storage import FileSystemStorage
# Create your views here.
def signup(request):
    return render(request,'./myapp/signup.html')
def test2(request):
    return render(request,'./myapp/test2.html')
def savepicture(request):
    return render(request,'./myapp/savepicture.py')
def contactview(request):
    uname = request.session['user_name']
    userobj = user_details.objects.get(email=uname)
    if request.method == 'POST':
        s = request.POST.get('title')
        content = request.POST.get('content')

        ul = contact(content=content,user=userobj,title=s)
        ul.save()
        return render(request,'./myapp/userindex.html')

    return render(request,'./myapp/contact.html')
def test(request):
    "Grab the whole screen"
    import pyscreenshot as ImageGrab

    # grab fullscreen
    im = ImageGrab.grab()


    # save image file
    im.save("media/webfullscreen.png")

    if request.method == 'POST':
        u_file = request.FILES['var image']

        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        uc = cimg(case_status=path)
        uc.save()

    return render(request,'./myapp/test.html')

def testpy(request):
    return render(request, './myapp/test.py')
def test1(request):
    if request.method == 'POST':
        u_file = request.FILES['captured_image_data']

        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        uc = cimg(case_status=path)
        uc.save()
    return render(request,'./myapp/test1.html')

def signup(request):
    if request.method =='POST':
        name=request.POST.get('name')
        birthday=request.POST.get('birthday')
        gender=request.POST.get('gender')
        img=request.POST.get('img')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        uname=email
        ul=user_login(uname=uname,password=password,u_type='user')
        ul.save()
        user_id=user_login.objects.all().aggregate(Max('id'))['id__max']
        ud=user_details(user_id=user_id,name=name,birthday=birthday,userphoto=img,gender=gender,email=uname, password=password,phone=phone)
        ud.save()
        context={'msg':'User Registered'}
        return redirect(login)
    else:
        context={'msg':'Not Registered'}
        return render(request, './myapp/signup.html',context)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
                      #table uname=
        ul = user_login.objects.filter(uname=uname, password=password, u_type='user')
        ua = user_login.objects.filter(uname=uname, password=password, u_type='admin')
        up = user_login.objects.filter(uname=uname, password=password, u_type='police')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname

            #send_mail('Login','welcome'+uname,uname)

            uname = request.session['user_name']
            userdetails = user_details.objects.filter(email=uname)
            viewpolicedetails = police_details.objects.all()
            newsdetailscollect = news.objects.all()

            context = {'uname': request.session['user_name'], 'ul': ul, 'details': viewpolicedetails,
                       'newsdisplay': newsdetailscollect, 'u': userdetails}

            return redirect(userindex)

        elif len(ua) == 1:
            request.session['user_id'] = ua[0].id
            request.session['user_name'] = ua[0].uname
            context = {'uname': request.session['user_name'],'ua':ua}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/admin/', context)

        elif len(up) == 1:
            request.session['user_id'] = up[0].id
            request.session['user_name'] = up[0].uname

            # send_mail('Login','welcome'+uname,uname)
            viewpolicedetails = police_details.objects.all()
            newsdetailscollect = news.objects.all()
            p = police_details.objects.filter(police_email=request.session['user_name'])
            vpd = {'details': viewpolicedetails, 'newsdisplay': newsdetailscollect, 'p': p,
                   'uname': request.session['user_name'], 'up': up}
            return redirect(policeindex)

        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/login.html', context)
    else:
        context = {'msg': 'No no no'}
        return render(request, 'myapp/login.html',context)

def policeindex(request):
    viewpolicedetails = police_details.objects.filter(rank='DGP')
    newsdetailscollect = news.objects.all().order_by('-id')[:3]
    p = police_details.objects.filter(police_email=request.session['user_name'])
    vpd = {'details': viewpolicedetails,'newsdisplay':newsdetailscollect, 'p': p}
    return render(request, './myapp/policeindex.html', vpd)


def delete(request):
    id = request.GET.get('id')
    d = news.objects.get(id=int(id))
    d.delete()

    return redirect(policeindex)


def userindex(request):
    uname = request.session['user_name']
    userdetails=user_details.objects.filter(email=uname)
    viewpolicedetails = police_details.objects.filter(rank='DGP')
    newsdetailscollect = news.objects.all().order_by('-id')[:3]
    vpd = {'details': viewpolicedetails,'newsdisplay':newsdetailscollect,'u':userdetails}
    return render(request, './myapp/userindex.html', vpd)

def policeaddnews(request):
    p = police_details.objects.filter(police_email=request.session['user_name'])
    v={'p':p}
    if request.method == 'POST':
        u_file = request.FILES['newsimg']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        newstitle = request.POST.get('newstitle')
        newscontent = request.POST.get('newscontent')

        uc = news(newstitle=newstitle, newscontent=newscontent, newsimg=path)
        uc.save()
        # ss = {'detail': uc,'p':p}
        return redirect(policeindex)
    else:
        return render(request, './myapp/policeaddnews.html',v)

#


def policehome(request):
    return render(request,'./myapp/policehome.html')
def userhome(request):
    return render(request,'./myapp/userhome.html')
def adminhome(request):
    return render(request,'./myapp/adminhome.html')
def about(request):
    uname = request.session['user_name']
    userdetails = user_details.objects.filter(email=uname)
    v={'u':userdetails}
    return render(request,'./myapp/about.html',v)

def filecomplaint(request):
    # ...............station list select in form...........
    stationselect = station.objects.all()
    uname = request.session['user_name']
    profiledisplay = user_details.objects.filter(email=uname)
    up = user_details.objects.get(email=uname)
    ss = {'details': stationselect,'u':profiledisplay}
    # .................station list ends...................
    if request.method =='POST':
        u_file = request.FILES['supportingdocument']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        complainttitle= request.POST.get('complainttitle')
        complaintdetails= request.POST.get('complaintdetails')
        suspect= request.POST.get('suspectdetails')
        address= request.POST.get('address')
        uname=request.session['user_name']
        userobj= user_details.objects.get(email=uname)
        phone = userobj.phone
        stationn= request.POST.get('stationn')
        uc= complaint(complaint_title=complainttitle,complaint_details=complaintdetails,phone=phone, suspect=suspect, address=address ,user=userobj, station=station. objects.get(station_name=stationn),supporting_doc=path)
        uc.save()
        ss = {'detail': uc,'u':profiledisplay}
        return render(request, './myapp/filecomplaint.html', ss)

    return render(request, './myapp/filecomplaint.html',ss)
def profile(request):
    uname = request.session['user_name']
    profiledisplay = user_details.objects.filter(email=uname)
    ss = {'details': profiledisplay}
    return render(request,'./myapp/profile.html',ss)

def policeprofile(request):
    uname = request.session['user_name']
    policeprofiledisplay = police_details.objects.filter(police_email=uname)
    ss = {'details': policeprofiledisplay}
    return render(request,'./myapp/policeprofile.html',ss)

def addcriminaldetails(request):
    # ...............station list select in form...........
    stationselect = station.objects.all()
    ss = {'details': stationselect}
    # .................station list ends...................
    if request.method =='POST':
        u_file = request.FILES['identity']
        u_filee = request.FILES['evidence']
        u_fileee = request.FILES['photo']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)
        pathh = fs.save(u_filee.name, u_filee)
        pathhh = fs.save(u_fileee.name, u_fileee)
        criminalname = request.POST.get('criminalname')
        criminal_date_of_birth= request.POST.get('criminal_date_of_birth')
        criminal_gender= request.POST.get('criminal_gender')
        criminal_email= request.POST.get('criminal_email')
        criminal_phone= request.POST.get('criminal_phone')
        criminal_address= request.POST.get('criminal_address')
        crime= request.POST.get('crime')
        registered_station= request.POST.get('registered_station')
        case_status= request.POST.get('case_status')
        uc= criminaldetails(criminalname=criminalname,photo=pathhh,criminal_phone=criminal_phone,evidence=pathh, criminal_email=criminal_email,identity= path, criminal_date_of_birth =criminal_date_of_birth, criminal_gender=criminal_gender,crime=crime, criminal_address=criminal_address ,registered_station=registered_station, case_status=case_status)
        uc.save()
        ss = {'detail': uc}
        return render(request, './myapp/addcriminaldetails.html', ss)
    return render(request, './myapp/addcriminaldetails.html', ss)

def police_view_criminals(request):
    p = criminaldetails.objects.all().order_by('-id')
    ss = {'details': p}
    return render(request,'./myapp/police_view_criminals.html',ss)
import os
def updatecriminalstatus(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        up = criminaldetails.objects.get(id=id)

        if len(request.FILES) != 0:
            if len(up.photo) > 0:
                os.remove(up.photo.path)
            up.photo = request.FILES['photo']


        criminalname= request.POST.get('criminalname')

        criminal_gender= request.POST.get('criminal_gender')
        criminal_email= request.POST.get('criminal_email')
        criminal_phone= request.POST.get('criminal_phone')
        crime = request.POST.get('crime')
        criminal_address = request.POST.get('criminal_address')
        case_status = request.POST.get('case_status')
        registered_station= request.POST.get('registered_station')

        up.criminalname = criminalname

        up.criminal_gender = criminal_gender
        up.criminal_email = criminal_email
        up.criminal_phone = criminal_phone
        up.crime = crime

        up.criminal_address= criminal_address
        up.case_status= case_status
        up.registered_station= registered_station
        up.save()


        context = {'msg': 'User Details Updated','up':up,'updatemsg':'product updated'}
        return redirect(police_view_criminals)

    else:
        id = request.GET.get('id')
        up = criminaldetails.objects.get(id=id)
        context={'up':up}
        return render(request, 'myapp/updatecriminalstatus.html',context)

def countdbobject(request):
    num = police_details.objects.all().count()
    vpd = {'num': num}
    return render(request, './myapp/policeviewcomplaints.html', vpd,num)

def policeviewcomplaints(request):
    complaintdetailscollect = complaint.objects.all()
    p  =police_details.objects.get(police_email=request.session['user_name'])
    s_id = request.GET.get('s_id')
    c=complaint.objects.filter(station=s_id).order_by('-id')
    if request.method == 'POST':
        user = request.GET.get('user')
        s = user_details.objects.filter(name=user)
        vpd = {'complaintdisplay': c, 's': s}
        return render(request, './myapp/policeviewcomplaints.html',vpd)
    user = request.GET.get('user')
    u=user_details.objects.filter(name=user)
    vpd = {'complaintdisplay': c,'u':u}
    return render(request, './myapp/policeviewcomplaints.html',vpd)


def policeupdatecomplaintstatus(request):

    complaintdetailscollect = complaint.objects.all()
    p = police_details.objects.filter(police_email=request.session['user_name'])

    # p  =police_details.objects.get(police_email=request.session['user_name'])
    s_id = request.GET.get('s_id')
    c=complaint.objects.filter(id=s_id)
    vpd = {'complaintdisplay':c}
    if request.method == 'POST':
        s_id = request.POST.get('id')
        up = complaint.objects.get(id=s_id)
        status= request.POST.get('status')
        up.status = status
        up.save()

        context = {'msg': 'complaint status Updated', 'up': up,'complaintdisplay':c,'p':p}
        return render(request, 'myapp/policeupdatecomplaintstatus.html', context)

    else:
       s_id = request.GET.get('s_id')
       up =  complaint.objects.get(id=s_id)
       context = {'up': up,'complaintdisplay':c,'p':p}
       return render(request, 'myapp/policeupdatecomplaintstatus.html', context)

      # return render(request, './myapp/policeupdatecomplaintstatus.html',vpd)


def user_view_complaint(request):
    complaintdetailscollect = complaint.objects.all()
    uname = request.session['user_name']
    userdetails = user_details.objects.filter(email=uname)
    c = complaint.objects.all().order_by('-id')[20:]
    p = user_details.objects.filter(email=request.session['user_name'])
    s_id = request.GET.get('s_id')

    d = complaint.objects.filter(user=s_id).order_by('-id')[:20]
    vpd = {'complaintdisplay': d, 'userdetail': p,'u':userdetails}
    return render(request, './myapp/user_view_complaint.html', vpd)



def updateprofile(request):
    uname = request.session['user_name']
    profiledisplay = user_details.objects.filter(email=uname)
    p = user_details.objects.get(email=uname)
    xemail=p.email
    ss = {'details': profiledisplay}
    if request.method == 'POST':
        uname = request.session['user_name']
        up = user_details.objects.get(email=uname)

        if len(request.FILES) != 0:
            if len(up.userphoto) > 0:
                os.remove(up.userphoto.path)
            up.userphoto = request.FILES['userphoto']
        # if request.FILES['userphoto']==0:
        #     pass
        # else:
        #   up.userphoto = request.FILES['userphoto']
        #   up.save()
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        up.name = name
        up.birthday = birthday
        up.gender = gender
        up.email = email
        up.password = password
        up.phone = phone
        up.save()

        u = user_login.objects.get(uname=xemail)
        u.uname = email
        u.password = password
        u.save()

        context = {'msg': 'User Details Updated','up':up,'updatemsg':'product updated','details': profiledisplay}
        return redirect(profile)

    else:
        user_id = request.session['user_id']
        up = user_details.objects.get(user_id=int(user_id))
        context={'up':up,'details': profiledisplay}
        return render(request, 'myapp/updateprofile.html',context)

def policeupdateprofile(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        upp = police_details.objects.get(id=id)
        x = police_details.objects.get(id=id)
        xemail=x.police_email

        if len(request.FILES) != 0:
            if len(upp.police_photo) > 0:
                os.remove(upp.police_photo.path)
            upp.police_photo = request.FILES['police_photo']

        police_name = request.POST.get('police_name')
        police_birthday = request.POST.get('police_birthday')
        police_gender = request.POST.get('police_gender')
        police_email = request.POST.get('police_email')
        police_password = request.POST.get('police_password')
        police_phone = request.POST.get('police_phone')
        upp.police_name = police_name
        # # up.birthday = birthday

        upp.police_gender = police_gender
        upp.police_email = police_email
        upp.police_password = police_password
        upp.police_phone = police_phone
        upp.save()


        up = user_details.objects.get(email=xemail)

        if len(request.FILES) != 0:
            if len(up.userphoto) > 0:
                os.remove(up.userphoto.path)
            up.userphoto = request.FILES['police_photo']

        up.name = police_name
        up.gender = police_gender
        up.email = police_email
        up.password = police_password
        up.phone = police_phone

        up.save()

        uname = request.session['user_name']
        u = user_login.objects.get(uname=xemail)
        u.uname = police_email
        u.password = police_password
        u.save()

        if xemail != upp.police_email:
            return redirect(login)


        context = {'msg': 'User Details Updated','upp':upp,'updatemsg':'profile updated','up':up}
        return redirect(policeprofile)

    else:
        # user_id = request.session['user_id']
        id = request.GET.get('id')
        upp = police_details.objects.get(id=id)
        # upp = police_details.objects.all()
        uname = request.session['user_name']
        up = user_details.objects.filter(email=upp.police_email)
        context={'upp':upp,'up':up}
        return render(request, 'myapp/policeupdateprofile.html',context)


def logout(request):
    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
        return login(request)
    else:
        return login(request)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from base64 import b64decode
from .models import ImageModel

@csrf_exempt
def save_image(request):

    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        image_data = image_data.replace('data:image/png;base64,', '')
        image_data = b64decode(image_data)
        image = ImageModel()
        image.image.save('image.png', ContentFile(image_data))
        image.save()
        return JsonResponse({'success': True})
    else:
        return render(request, 'myapp/test1.html')

from django.shortcuts import render
from django.http import JsonResponse
from .models import WebcamImage

def test3(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        image = WebcamImage.objects.create(image=image_data)
        image.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def test4(request):

   if request.method == 'POST':
       import base64

       img = request.POST['image'];
       folderPath = "media/";
       image_parts = img.split(";base64,");
       image_type_aux = image_parts[0].split("image/");
       image_type = image_type_aux[1];
       image_base64 = str(base64.b64decode(image_parts[1]), "utf-8");
       filename = uniqid() + '.png';
       file = str(folderPath) + str(filename);
       file_put_contents(file, image_base64);
       print(filename);


def usersave(request):
    if request.method == 'POST':

        u = request.FILES['photo']
        fs = FileSystemStorage()
        path = fs.save(u.name, u)
        uc = xx(User_pic=path)
        uc.save()

        return render(request, './myapp/some.html')
    else:
        return render(request, './myapp/some.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_image(request):
  # Get the image data from the POST request
  image_data = request.POST.get('image')

  # Save the image to your model
  my_model = MyModel(image=image_data)
  my_model.save()

  # Return a success response
  return JsonResponse({'success': True})
  # return render(request, 'myapp/save_image.html')

def policeviewrelatedcrimes(request,suspect):


    suspectt=complaint.objects.filter(suspect=suspect)
    p = criminaldetails.objects.filter(criminalname=suspect).order_by('-id')


    return render(request, './myapp/policeviewrelatedcrimes.html',{'suspect':suspectt,'details':p})


def test6(request):
    path = request.POST["src"]
    image = NamedTemporaryFile()
    image.write(urlopen(path).read())
    image.flush()
    image = File(image)
    name = str(image.name).split('\\')[-1]
    name += '.jpg'
    image.name = name
    obj = image.objects.create(image=image)
    obj.save()
    return render(request,'./myapp/test6.html')
