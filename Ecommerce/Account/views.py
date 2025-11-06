from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login
User = get_user_model()
# Create your views here.
def base(request):
    return render(request,'base.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone_number=  request.POST.get('phone_number')
        city = request.POST.get('city')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')
        if password!=confirmpass:
            return redirect('signup_view')
        else:
            my_user = User.objects.create_user(email=email,first_name=first_name,last_name=last_name,dob=dob,address=address,phone_number=phone_number,city=city,password=password)
            print(my_user)
            print(first_name)
            my_user.save()
        return redirect('login_view')
    return render(request,'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user= User.objects.get(email=email)
            if user.check_password(password):
                auth_login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Wrong password")
        except:
            return HttpResponse("No user found")
    return render(request,'login.html')
