
from django.contrib import admin
from django.urls import path,include
from dealer import views

urlpatterns = [
# basic Url
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('pricing',views.price, name="price"),
    path('contact',views.contact, name="contact"),
    path('about',views.about,name="about"),
    path('market', views.market, name="market"),
    path('book_lead',views.book_lead, name="book_lead"),
    path('signup', views.signup, name="Sign up"),
    path('add_signup', views.add_signup, name="create Dealer"),
    path('signout',views.signout, name="signout"),
    path('dealer', include('dealerapp.urls',  namespace='dealerapp')),
    path('leaseadmin/',include('leasadmin.urls', namespace='leaseadmin')),

]