from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, db_column="customer_id")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField()
    monthly_salary = models.BigIntegerField()
    approved_limit = models.BigIntegerField(null=True, blank=True)
    current_debt = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} -- {self.last_name}"


class Loan(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_id = models.IntegerField()
    loan_amount = models.IntegerField()
    tenure = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=2, decimal_places=2)
    monthly_emi = models.IntegerField()
    emi_paid_on_time = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
