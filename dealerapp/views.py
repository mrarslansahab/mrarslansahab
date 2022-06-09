from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import dealer
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request,"login.html")


def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        if dealer.objects.filter(email=email, password=password).exists():
            if dealer.objects.filter(email=email,password=password,status="approved"):
                request.session['email'] = email
                request.session['password'] = password
                return redirect('/market')
            elif dealer.objects.filter(email=email,password=password,status="rejected"):
                messages.error(request, "Your Account is Rejected please contact our Support For further Assistance Thanks !", extra_tags="error")
                return redirect('/dealer')
            else:
                messages.warning(request,"Your Account is Still pending please Wait or  contact our Support For further Assistance Thanks !",extra_tags="warning")
                return redirect('/dealer')

        else:
            messages.error(request,"Please Enter Correct email or password !", extra_tags="error")
            return redirect('/dealer')
    else:
        return HttpResponse("You are trying Wrong method !")