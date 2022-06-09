from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.


class user_accounts(models.Model):
    name=models.CharField(max_length=64, null=True)
    email=models.EmailField(max_length=64, null=True)
    password=models.CharField(max_length=64, null=True)
    role=models.CharField(max_length=64, null=True)
    user_name=models.CharField(max_length=64, null=True)
    created_by = models.CharField(max_length=64, null=True)
    deleted_by = models.CharField(max_length=64, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=64, null=True)

class dealer_types(models.Model):
    name=models.CharField(max_length=64, null=True)
    detail=models.CharField(max_length=64, null=True)
    created_by = models.CharField(max_length=64, null=True)
    deleted_by = models.CharField(max_length=64, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=64, null=True)