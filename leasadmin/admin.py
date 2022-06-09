from django.contrib import admin
from dealerapp.models import dealer,package,b_leads
from leasadmin.models import user_accounts,dealer_types
# Register your models here.


admin.site.register(dealer)
admin.site.register(b_leads)
admin.site.register(package)
admin.site.register(user_accounts)
admin.site.register(dealer_types)