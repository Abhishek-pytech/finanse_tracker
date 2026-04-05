from rest_framework import routers
from .views import TransactionViewSet
from django.contrib import admin
from django.urls import path, include
from transactions.views import summary



router=routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('summary/', summary)
]  + router.urls


