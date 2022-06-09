from django.shortcuts import render,redirect
from django.http import HttpResponse
from dealerapp.models import dealer,b_leads
from django.contrib import messages
from .models import dealer_types,user_accounts


def login(request):
    return render(request, "admin-login.html")

def index(request):
    if 'password' in request.session:
        return render(request, "dashboard.html")
    else:
        messages.warning(request, "Please Log in First Thanks !", extra_tags="warning")
        return redirect('/leaseadmin')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if user_accounts.objects.filter(email=email,password=password):
            return render(request, "dashboard.html")
        else:
            messages.error(request,"Please Enter Correct email or Password Thanks !", extra_tags="error")
            return redirect('/leaseadmin')
def dealersaccount(request):
    obj=dealer.objects.all()
    obj2=dealer.objects.filter(status="approved")
    obj3=dealer.objects.filter(status="pending")
    obj4=dealer.objects.filter(status="rejected")
    obj5=dealer_types.objects.all()
    context={'ald':obj, 'aad':obj2, 'apd':obj3, 'ard':obj4, 'dts':obj5}
    return render(request, "dealers.html", context)


def update_dealer(request):
    if request.method=='POST':
        id=request.POST['edit_id']
        obj=dealer.objects.get(id=id)
        obj.f_name=request.POST['edit_f_name']
        obj.l_name=request.POST['edit_l_name']
        obj.cvrno=request.POST['edit_cvr']
        obj.package=request.POST['edit_package']
        obj.email=request.POST['edit_email']
        obj.contact=request.POST['edit_contact']
        obj.telephone=request.POST['edit_telephone']
        obj.telephone=request.POST['edit_telephone']
        obj.dealer_type_id=request.POST['edit_dealer_type']
        obj.postal_code=request.POST['edit_postal_code']
        obj.city=request.POST['edit_city']
        obj.address=request.POST['edit_address']
        obj.status=request.POST['edit_status']
        obj.save()
        messages.success(request,"Account " + obj.status + " Successfully !", extra_tags="success")
        return redirect('leaseadmin:dealers')
    else:
        return HttpResponse("You Try Wrong Method")


def leads(request):
    obj=b_leads.objects.all()
    context={'ld':obj}
    return render(request,"leads.html",context)