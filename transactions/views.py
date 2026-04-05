from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Transaction
from .serializer import TransactionSerializer
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user.is_staff
    


    

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_class=[IsAdminOrReadOnly]

    def get_queryset(self):
        queryset=Transaction.objects.all()

        type_param= self.request.query_params.get('type')

        category= self.request.query_params.get('category')

        date=self.request.query_params.get('date')

        if type_param:
            queryset=queryset.filter(type=type_param)
        if category:
            queryset=queryset.filter(category=category)
        if date:
            queryset=queryset.filter(date=date)

        return queryset



@api_view(['GET'])
def summary(request):
    income = Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0

    expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense,
    })

