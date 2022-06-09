from django.shortcuts import render,redirect
import  requests
from django.http import HttpResponse
from django.contrib import  messages
from dealerapp.models import dealer,package,b_leads
from leasadmin.models import dealer_types

# Create your views here.
def index(request):
    active = "active"
    context = {'hm': active}
    return render(request, "index.html", context)
def market(request):
    if 'password' in request.session:
        active = "active"
        leads = requests.get('https://3leasingtilbud.pipedrive.com/api/v1/stages/11/deals?api_token=8d2bef77604e61380e5ca25f330e659b1ea8be7b').json()
        person = requests.get('https://3leasingtilbud.pipedrive.com/api/v1/persons?api_token=8d2bef77604e61380e5ca25f330e659b1ea8be7b').json()
        booked_leads=b_leads.objects.all()
        email=request.session['email']
        password=request.session['password']
        obj=dealer.objects.get(email=email,password=password,status="approved")
        context = {'mp': active, 'leads':leads, 'person': person,'nm':obj,'bl':booked_leads}
        return render(request, "market_place.html", context)
    else:
        return redirect('/dealer')
def book_lead(request):
    if request.method=='POST':
        obj=b_leads()
        obj.deal_name=request.POST['deal_name']
        obj.car_name=request.POST['car_name']
        obj.booked_by=request.POST['booked_by']
        obj.dealer_id=request.POST['dealer_id']
        obj.rating=request.POST['rating']
        obj.dkk=request.POST['dkk']
        obj.price=request.POST['price']
        obj.deal_id=request.POST['deal_id']
        obj.save()
        d_id=request.POST['deal_id']
        dea_id=request.POST['dealer_id']
        bp=dealer.objects.get(id=dea_id)
        bp.booked_leads=bp.booked_leads+1
        bp.save()
        payload={'label':216,'stage_id':11}
        requests.put('https://3leasingtilbud.pipedrive.com/api/v1/deals/'+d_id+'?api_token=8d2bef77604e61380e5ca25f330e659b1ea8be7b', data=payload)
        messages.success(request,"Leads Booked Successfully", extra_tags="success")
        return redirect('/market')
    else:
        return HttpResponse("You are Trying Wrong Method")



def signout(request):
    return redirect('/dealer')
def signup(request):
    dealer=dealer_types.objects.all()
    obj=package.objects.all()
    context={'dealer': dealer,'obj':obj}
    return render(request, "signup.html",context)
def add_signup(request):
    if request.method=='POST':
        obj=dealer()
        obj.package_id=request.POST['pacakge']
        obj.f_name=request.POST['fname']
        obj.email=request.POST['email']
        obj.contact=request.POST['contact']
        obj.address=request.POST['address']
        obj.postal_code=request.POST['postal_code']
        obj.l_name=request.POST['lname']
        obj.Telephone=request.POST['telephone']
        obj.cvrno=request.POST['cvrno']
        obj.city=request.POST['city']
        obj.status="pending"
        obj.dealer_type_id=request.POST['dealer_type']
        obj.is_deleted="0"
        obj.password=request.POST['password']
        obj.save()
        messages.success(request,"You are successfully Signup One of Over Team member contact you ASAP !", extra_tags="success")
        return redirect('/signup')

def price(request):
    return render(request,"pricing.html")


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")