from django.db import models
from leasadmin.models import user_accounts,dealer_types
#Admin Side


class package(models.Model):
    name=models.CharField(max_length=40, null=True)
    details=models.CharField(max_length=40, null=True)
    is_deleted = models.IntegerField(null=True)
    deleted_by = models.CharField(max_length=64, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=64, null=True)


# Dealer Side
class dealer(models.Model):
    f_name = models.CharField(max_length=64, null=True)
    l_name = models.CharField(max_length=64, null=True)
    contact = models.CharField(max_length=64, null=True)
    cvrno = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=64, null=True)
    postal_code = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=100, null=True)
    Telephone = models.CharField(max_length=100, null=True)
    dealer_type = models.ForeignKey(dealer_types, related_name="d_type", on_delete=models.CASCADE, null=True)
    password=models.CharField(max_length=64, null=True)
    status = models.CharField(max_length=64, null=True)
    is_deleted = models.IntegerField(null=True)
    deleted_by = models.CharField(max_length=64,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=64,null=True)
    package = models.IntegerField( null=True)
    booked_leads=models.IntegerField( null=True)


class b_leads(models.Model):
    deal_id=models.IntegerField(max_length=40, null=True)
    phone=models.CharField(max_length=40, null=True)
    car_name=models.CharField(max_length=40, null=True)
    deal_name=models.CharField(max_length=50, null=True)
    rating=models.CharField(max_length=50, null=True)
    dkk=models.CharField(max_length=50, null=True)
    price=models.CharField(max_length=50, null=True)
    booked_by=models.CharField(max_length=50, null=True)
    dealer=models.ForeignKey(dealer,on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

