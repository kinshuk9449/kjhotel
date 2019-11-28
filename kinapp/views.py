from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import KjHotel,details,data
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
import datetime
from datetime import date
from django.utils.dateparse import parse_date

def index(request):
    return render(request,'index.html')
def delhi(request):
    det =details.objects.all().filter(city='Delhi')
    return render(request,'delhi.html',{'detail_list': det})

def hyderabad(request):
    det =details.objects.all().filter(city='Hyderabad')
    return render(request,'hyderabad.html',{'detail_list': det})

def mumbai(request):
    det =details.objects.all().filter(city='Mumbai')
    return render(request,'mumbai.html',{'detail_list': det})

def ludhiana(request):
    det =details.objects.all().filter(city='Ludhiana')
    return render(request,'ludhiana.html',{'detail_list': det})

def register(request):
    if request.method == 'POST':
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        prof = request.FILES
        profile = prof['profile']
        
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.success(request,'Email already exisit!!!!')
                return redirect('register')
            else:
                            kj =KjHotel(email=email,mobile=mobile,profile=profile)
                            user = User.objects.create_user(username=email,email=email,first_name=fname,last_name=lname,password=password)
                            user.save()
                            kj.save()
                            send_mail(
                                'Registration succesful',
                                'Thank you '+fname+' '+lname+' for registring with us. Hope you have a great experience with us.',
                                'jainkinshuk112@gmail.com',
                                [email],
                                fail_silently=False,
                            )
                            messages.success(request,'Registration succesful!!!')
                            return redirect('login')
        else:
            messages.error(request,'Password did not matched')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['psw']
        verify = authenticate(username=email1,password=password1)
        if verify is not None:
            auth.login(request,verify)
            return redirect('/')
        else:
            messages.error(request,'Invalid login details!!!!')
            return redirect('login')
    else:
        context = {}
        return render(request,'login.html',context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You have succesfully logout!!!!')
        return redirect("/")

def booking(request,hotel_name):
    det = details.objects.all().filter(hotel_name=hotel_name)
    if request.method =="POST":
        email=request.user.email
        hotel_name = request.POST['hotel_name']
        city = request.POST['city']
        hotel = hotel_name+","+city
        checkin1 = request.POST['checkin']
        checkin = parse_date(checkin1)
        checkout1 = request.POST['checkout']
        checkout = parse_date(checkout1)
        amount = request.POST['total']
        book =data(email=email,checkin=checkin,amount=amount,checkout=checkout,hotel=hotel)
        book.save()
        send_mail(
                    'Booking succesful',
                    'Your booking of hotel '+ hotel_name+','+city+'is done. Hope you enjoy your stay there.',
                    'jainkinshuk112@gmail.com',
                    [email],
                    fail_silently=False,
                )
        return redirect('confirm')
    else:
        return render(request,'booking.html',{'detail_list':det})

def confirm(request):
    
    return render(request,'confirm.html')
def oldbooking(request):
    data2 = data.objects.all().filter(email=request.user.email)
    return render(request,'oldbooking.html',{'data_list':data2})