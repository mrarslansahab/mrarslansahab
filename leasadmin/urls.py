
from django.contrib import admin
from django.urls import path,include
from leasadmin import views


app_name='leaseadmin'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard',views.index, name="dashboard"),
    path('dealersaccounts',views.dealersaccount, name="dealers"),
    path('leads',views.leads,name="leads"),
    path('update_dealer/',views.update_dealer, name="Update-dealer"),
    path('',views.login, name="log_in"),
    path('admin_signin',views.signin, name="sign_in")
]
