from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'
		
	def validate_type(self, value):
		if value not in ['income', 'expense']:
			raise serializers.ValidationError("Type must be 'income' or 'expense' ")
		return value
	def valide_amount(self, value):
		if value<=0:
			raise serializers.ValidationError("Amonut must be grater than 0")
		return value

		
		

    
	
