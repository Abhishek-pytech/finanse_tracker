from django.contrib import admin
from .models import Transaction
# Register your models here.
admin.site.site_header= "Finance Tracker Admin"
admin.site.site_title ="Finance Admin Panel"
admin.site.index_title= "Welcome to Finance Dashboard"
admin.site.register(Transaction)
