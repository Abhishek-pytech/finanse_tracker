from django.db import models

# Create your models here.
class Transaction(models.Model):
    type_choices=(('income', 'Income'),
                  ('expense', 'Expense'),

                  )
    amount=models.FloatField()
    type=models.CharField(max_length=10, choices=type_choices)
    category=models.CharField(max_length=100)
    date=models.DateField()
    notes= models.TextField(blank=True)



    def __str__(self):
        return f"{self.type} - {self.amount}"
